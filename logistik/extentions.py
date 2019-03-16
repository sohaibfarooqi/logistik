from flask_migrate import Migrate
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

"""
Register all extentions here.
"""
api_manager = APIManager()
db = SQLAlchemy()
migrate = Migrate()
swagger = Swagger()
