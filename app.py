from flask import Flask
from database_folder.database import initialize_db
import json
from flask_restful import Api
from resource_folder.routes import initialize_routes
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)
app.config.from_envvar('ENV_FILE_LOCATION')
app.config['MONGODB_SETTINGS'] = {
 'host': 'mongodb://localhost/card_database'
 }

initialize_db(app)
jwt = JWTManager(app)
initialize_routes(api)

app.run()