from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from config import config


mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'You must be logged in to access this page.'


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.py', silent=True)

    Bootstrap(app)
    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
