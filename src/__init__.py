from decouple import config
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(
    __name__, static_folder="../swagger/static", template_folder="../swagger/templates"
)
app.config.from_object(config("APP_SETTINGS"))

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Registering blueprints
from .controller.system import system_bp

app.register_blueprint(system_bp)
