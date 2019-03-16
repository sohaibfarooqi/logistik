import os
from .logistik.app import init_app

settings = os.environ.get("FLASK_SETTING_MODULE", 'logistik.logistik.settings.DevelopmentSettings')
app = init_app(settings)
