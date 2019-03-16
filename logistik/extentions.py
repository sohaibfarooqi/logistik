from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager

"""
Register all extentions here.
"""
api_manager = APIManager()
db = SQLAlchemy()
migrate = Migrate()
