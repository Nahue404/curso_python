#!/usr/bin/env python 3 -- requiere de python 3
from flask import Flask
from login import login

app = Flask(__name__)

##servicios rest
app.register_blueprint(login)

@app.route('/', methods=['GET'])
def hello():
    return '¡Hola, mundo!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)