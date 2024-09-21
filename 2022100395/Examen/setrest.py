#!/usr/bin/env python
# -*- Coding: utf-8 -*-
"""
Autor      : Nahuel Riveros
Fecha      : 21/09/2024

Nombre     : setrest
Objetivo   : Se encarga de realizar scraping en la pagina del jaguarete ingresando matricula y contraseña, se guarda en una bd los datos.
"""

from flask import Flask, Blueprint, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import mysql.connector
from datetime import datetime
from time import sleep

app = Flask(__name__)
setrest01 = Blueprint('setrest01', __name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '124',
    'database': 'curso_python'
}

@app.route('/setrest01', methods=['POST'])
def llamarServicioSet():
    codigo = request.json['codigo']
    password = request.json['password']
    
    salida = inicializarVariables(codigo, password)
    
    return jsonify({'ParmOut': salida})

def inicializarVariables(codigo, password):
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--ignore-certificate-errors')
    chromedriver_path = 'C:\\Users\\usuario\\Documents\\Nahuel\\1UNIVERSIDAD\\1Python\\python\\2022100395\\Clase6\\chromedriver.exe'
    
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_page_load_timeout(15)
    
    try:
        driver.get('https://jaguarete.unida.edu.py/jaguarete/Login')
        accesoSet(driver, codigo, password)
    except TimeoutException:
        driver.close()
        driver.quit()
        print("No se pudo abrir la página Jaguarete!!!")
    finally:
        driver.quit()

def accesoSet(driver, codigo, password):
    url_jaguarete = 'https://jaguarete.unida.edu.py/jaguarete/Login'
    
    try:
        codigo_input = driver.find_element(By.ID, 'codigo')
        codigo_input.send_keys(codigo)
        sleep(5)
        password_input = driver.find_element(By.ID, 'password')
        password_input.send_keys(password)
        sleep(5)
        
        login_button = driver.find_element(By.XPATH, '//*[text()="Ingresar"]')
        login_button.click()
        sleep(5)
        
        registrar_evento(codigo, url_jaguarete)
        
    except Exception as e:
        print("ERROR EN: login, intentando cerrar el driver", str(e))
    
def registrar_evento(matricula, url_visita):
    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()
        
        query = """INSERT INTO registros_autenticacion (matricula, url_visita, fecha_hora)
                   VALUES (%s, %s, %s)"""
        fecha_hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(query, (matricula, url_visita, fecha_hora_actual))
        
        conexion.commit()
    
    except mysql.connector.Error as err:
        print(f"Error al registrar en la base de datos: {err}")
    
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

if __name__ == '__main__':

    codigo = input("Ingrese su número de matrícula: ")
    password = input("Ingrese su contraseña: ")
    
    app.register_blueprint(setrest01)
    
    inicializarVariables(codigo, password)
    
    app.run(host='0.0.0.0', port=5000)
