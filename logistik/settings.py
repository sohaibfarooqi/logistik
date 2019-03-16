import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Settings(object):
  """
  Base class for Flask settings.
  """
  DEBUG = False
  TESTING = False
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'local.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionSettings(Settings):
  """
  Use this class to override any special settings for production
  """
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')

class DevelopmentSettings(Settings):
  """
  Use this class to override any special settings for development
  """
  DEBUG = True

class TestingSettings(Settings):
  """
  Use this class to override any special settings for testing
  """
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'testing.db')
  TESTING = True
  SERVER_NAME = "127.0.0.1:5555"
