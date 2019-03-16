import os
from functools import partial

from flask import Flask
from flasgger import swag_from
from flasgger import Swagger
from .extentions import api_manager, db, migrate, swagger
from .models import all_models
from .views import BASE_PREFIX, blueprints


def init_app():
    """
    Function to initilize Flask app and register
    extentions.
    """
    app = Flask(__name__)
    settings = os.environ.get("FLASK_SETTING_MODULE",
                              'logistik.settings.DevelopmentSettings')
    app.config.from_object(settings)
    with app.app_context():
        register_crud_api(app)
        register_extensions(app)
        register_blueprints(app)
    return app


def register_extensions(app):
    """
    Register all external extentions.
    """
    db.init_app(app)
    migrate.init_app(app, db)
    api_manager.init_app(app, flask_sqlalchemy_db=db)
    swagger.init_app(app)


def register_blueprints(app):
    """
    Register all Blueprints.
    """
    for bp in blueprints:
        app.register_blueprint(bp)


def register_crud_api(app):
    """
    Register CRUD Api for all models.
    """
    http_methods = ('GET', 'POST', 'PUT', 'DELETE',)
    for model in all_models:
        exclude = model._exclude
        api_manager.create_api(
            model, methods=http_methods, url_prefix=BASE_PREFIX, exclude_columns=exclude)
