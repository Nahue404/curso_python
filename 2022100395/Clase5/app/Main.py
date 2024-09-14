from flask import Flask
from urllib.parse import quote as url_quote
from flask_swagger_ui import get_swaggerui_blueprint
from login import login 

app = Flask(__name__)

app.register_blueprint(login)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Login API"  
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/', methods=['GET'])
def hello():
    return 'hola'

if __name__ == '__main__':
 app.run(host='0.0.0.0', debug= True, port=5001)