#!/usr/bin/env python
# -*- Coding: utf-8 -*-

from flask import Blueprint, request, jsonify
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import os, signal
from time import sleep
import pandas as pd
from unipath import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
 
setrest01 = Blueprint('setrest01', __name__)

@setrest01.route('/setrest01', methods=['POST'])
def llamarServicioSet():
    global codigo, password
    ##try:
    codigo =request.json['codigo']
    password =request.json['password']
    inicializarVariables(codigo,password)
    
     
    salida = {'codRes': codRes, 'menRes': menRes}
    return jsonify({'ParmOut':salida})

def inicializarVariables(codigo,password):
    global codRes, menRes, driver, PID
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    
    # Configuración de las opciones de Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Iniciar Chrome maximizado
    chrome_options.add_argument('--ignore-certificate-errors')
    #chrome_options.add_argument("--test-type")
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--no-sandbox')
    chromedriver_path = 'C:\Users\usuario\Documents\Nahuel\1UNIVERSIDAD\1Python\python\2022100395\Clase6\chromedriver.exe'
    # Inicializa el servicio de ChromeDriver
    service = Service(chromedriver_path)

    # Crea una instancia del navegador Chrome
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_page_load_timeout(15)            
    try:
            driver.get('https://jaguarete.unida.edu.py/jaguarete/Login')
            accesoSet(codigo,password)
    except TimeoutException:
            driver.close()
            driver.quit()
            print("No se pudo abrir la pagina jaguarete !!!")


def accesoSet(codigo,password):
    global menRes,codRes
    

    try:
        codigo = driver.find_element(By.ID, 'codigo')
        codigo.send_keys("2022100395")
        sleep(5)
        password = driver.find_element(By.ID, 'password')
        password.send_keys("shasj")
        sleep(5)
        login = driver.find_element(By.XPATH, '//*[text()="Ingresar"]')
        login.click()
        sleep(5)
        driver.close()
        driver.quit()
        
             
    except Exception as e:
        print("ERROR EN: login, intento driver.close() - driver.quit",str(e))
        driver.close()
        driver.quit()
        print("ERROR EN: login, termine driver.close() - driver.quit")
