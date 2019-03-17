import os
from functools import partial

from flask import Flask, jsonify
from .extentions import api_manager, db, migrate, swagger
from .models import all_models
from .views import BASE_PREFIX, blueprints
from .error_handlers import page_not_found, intenal_server_error


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
        app.register_error_handler(404, page_not_found)
        app.register_error_handler(500, intenal_server_error)
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

def register_errorhandlers(app):
    """Register error handlers."""
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        print(error)
    #     error_code = getattr(error, 'code', 500)
    #     return render_template('{0}.html'.format(error_code)), error_code
    # for errcode in [401, 404, 500]:
    #     app.errorhandler(errcode)(render_error)
    # return None
        return jsonify({"Error": 500})
