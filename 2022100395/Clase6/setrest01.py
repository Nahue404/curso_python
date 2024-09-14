#!/usr/bin/env python
# -*- Coding: utf-8 -*-
"""
Modulos    : Descargar de RUC
Sub-Modulos: RUC
Empresa    : Vision Banco S.A.E.C.A

Autor      : Derlis Caballero
Fecha      : 30/01/2020

Nombre     : setrest01
Objetivo   : Se encarga de realizar scraping en la pagina de la SET para
descargar zip de ruc por controlm

Tipo       : Servicio SET

Ej. llamada:
http://10.13.100.9:5000/setrest01
{
	"act":"ruc2"
}
"""
from flask import Blueprint, request, jsonify
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import os, signal
from time import sleep
import pandas as pd
from unipath import Path
 
setrest01 = Blueprint('setrest01', __name__)

@setrest01.route('/setrest01', methods=['POST'])
def llamarServicioSet():
    global act
    ##try:
    act =request.json['act']
    inicializarVariables(act)
    
     
    salida = {'codRes': codRes, 'menRes': menRes}
    return jsonify({'ParmOut':salida})

def inicializarVariables(act):
    global codRes, menRes, driver, PID
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    #Ruta para windows
    mainpath= "C:\Users\Default\Desktop"
    
    #Ruta para Linux
    #mainpath="/mnt/set/"
    fullpath= os.path.join(mainpath)
    options = webdriver.ChromeOptions()
    #Driver para linux descomentar o comentar de acuerdo al entorno
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    #driver = webdriver.Chrome(chrome_options=options, executable_path=r'/opt/chrome/chromedriver')
    #Driver para Windows
    #driver = webdriver.Chrome(chrome_options=options, executable_path=r'E:\\Compartida\\chrome\\chromedriver.exe')
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\usuario\Documents\Nahuel\1UNIVERSIDAD\1Python\python\2022100395\Clase6\chromedriver.exe')
    print(driver)
    PID = driver.service.process.pid ##ID proceso Chromedriver
    print('PID: ' + str(PID))
    ##driver.implicitly_wait(10)
    driver.set_page_load_timeout(15)            
    try:
            driver.get('https://www.set.gov.py/portal/PARAGUAY-SET/Home')
            accesoSet(fullpath,act)
    except TimeoutException:
            driver.close()
            driver.quit()
            print("Page load Timeout Occured EN: get a SET. Quiting !!!")


def accesoSet(fullpath,act):
    global menRes,codRes
    f = Path(fullpath)
    f.exists()

    try:
        print(fullpath)
        informes=driver.find_element_by_id('InformesPeriodicos')
        informes.click()
        print("Se ingreso en la menu de Informes Periódicos")
        tasasPasivas=driver.find_element_by_xpath('//*[@id="UICLVPresentation_3ef26739-4d0b-49da-a001-c50b530f979c"]/div/div[2]/a[14]')
        tasasPasivas.click()
        ruc=driver.find_element_by_link_text(act+'.zip')
        print("Accedu a la opcion zip")
        ruc.click()
        enable_downoad_headless(driver, fullpath)
        submit_button = driver.find_elements_by_xpath('/html/body/div[5]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[6]/div/div/div/div/div/div/div/div/div/div/div/div[3]/div/div[1]/div[2]/div/div/div[2]/a[1]')[0]
        submit_button.click()
        
        sleep(3)
             
    except Exception as e:
        print("ERROR EN: login, intento driver.close() - driver.quit",str(e))
        driver.close()
        driver.quit()
        matarChromeDriver()
        print("ERROR EN: login, termine driver.close() - driver.quit")

def enable_downoad_headless(browser,download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)
def matarChromeDriver():
    print('El PID quedo vivo: ' + str(PID))
    try:
        os.kill(PID, signal.SIGTERM) 
        print('Mate el proceso chromedriver: ' + str(PID))
    except OSError:
        print('Error al intentar matar el PID: ' + str(PID))
        pass