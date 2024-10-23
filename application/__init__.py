import binascii
from dotenv import load_dotenv
from flask import Flask, send_from_directory
from flask_socketio import SocketIO

load_dotenv()
import os
import traceback

from botocore.exceptions import ClientError
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from pydantic import ValidationError
from werkzeug.exceptions import NotFound, MethodNotAllowed

from application.utils.output import OutputObj
from application.utils.output import return_json
from config.DBConfig import DB_SETUP
from exceptions.custom_exception import CustomException
from flask_cors import CORS

app = Flask(__name__)
socketio = SocketIO(app)
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "https://horizonvaut.com"]}}, supports_credentials=True)
app.app_context().push()
SECRET_KEY = os.getenv('SECRET_KEY')
app.config['SECRET_KEY'] = SECRET_KEY
app.config["ENVIRONMENT"] = "local"
environment = str(app.config["ENVIRONMENT"]).lower()
print(f"APPLICATION IS RUNNING ON : {environment}")

jwt = JWTManager(app)

database = DB_SETUP[environment]

if not database:
    raise EnvironmentError

username = database['username']
password = database['password']
host = database['host']
database_name = database['database']

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@{host}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 10,
    'max_overflow': 20,
}
db: SQLAlchemy = SQLAlchemy(app)
metadata = db.metadata


@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('utils/images', filename)


@app.route('/fonts/<path:filename>')
def serve_fonts(filename):
    return send_from_directory('utils/fonts', filename)


@app.errorhandler(Exception)
def error_handling(error):
    traceback.print_exc()
    message = 'Internal server error!!!!!'
    code = 500
    response_code = 1000
    if isinstance(error, ClientError):
        message = error.response.get('Error', {}).get('Code') + " : " + error.response.get('Error', {}).get('Message')
        code = 400

    elif isinstance(error, binascii.Error):
        message = str(error) + ":" + "invalid image"
        response_code = 1000
        code = 400
    elif isinstance(error, CustomException):
        message = error.message
        response_code = error.response_code
        code = error.status_code
    elif isinstance(error, ValidationError):
        message = "Enter valid data"
        code = 400
    elif isinstance(error, NotFound):
        message = "Incorrect API Address"
        code = 400
    elif isinstance(error, MethodNotAllowed):
        message = "The request method is not allowed"
        code = 400
    else:
        error = CustomException()
        message = error.message
        code = error.status_code
        db.session.close()

    output = OutputObj(code=code, message=message, response_code=response_code)
    return return_json(output)
