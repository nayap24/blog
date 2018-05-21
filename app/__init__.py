from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_pagedown import PageDown
from flask_sqlalchemy import SQLAlchemy

from config import config


mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'You must be logged in to access this page.'
moment = Moment()
pagedown = PageDown()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.py', silent=True)
    config[config_name].init_app(app)

    Bootstrap(app)
    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)
    pagedown.init_app(app)

    from app.errors import errors as errors_blueprint
    app.register_blueprint(errors_blueprint)
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
