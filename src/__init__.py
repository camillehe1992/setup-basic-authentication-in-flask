import logging
from decouple import config
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(
    __name__, static_folder="../swagger/static", template_folder="../swagger/templates"
)
app.config.from_object(config("APP_SETTINGS", default="src.config.DevelopmentConfig"))

# Setup logging
log_level = logging.DEBUG if app.config["DEBUG"] else logging.INFO
app.logger.setLevel(level=log_level)
logger = app.logger

# Integrate with packages
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Registering blueprints
from .controller.auth import auth_bp
from .controller.swagger import swagger_bp
from .controller.system import system_bp
from .controller.user import user_bp

app.register_blueprint(auth_bp)
app.register_blueprint(swagger_bp)
app.register_blueprint(system_bp)
app.register_blueprint(user_bp)

# Import all models for migration under model folder
# Note: YOU NEED TO import new model file in model/__init__.py so that it can be detected by migration process
from .model import *
