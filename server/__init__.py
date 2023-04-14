from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_login import LoginManager
import os
from dotenv import load_dotenv

db = SQLAlchemy()
login_manager = LoginManager()
load_dotenv()
APP_KEY = os.getenv("APP_SECRET_KEY")


def create_app():
    app_obj = Flask(__name__, template_folder="../templates", static_folder="../static")
    app_obj.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app_obj.config["SECRET_KEY"] = APP_KEY

    db.init_app(app_obj)
    login_manager.init_app(app_obj)

    # Blueprint for auth routes in app
    from .auth import auth as auth_blueprint

    app_obj.register_blueprint(auth_blueprint)

    # Blueprint for non-auth routes in app
    from .app import main as app_blueprint

    app_obj.register_blueprint(app_blueprint)

    with app_obj.app_context():
        db.create_all()

    return app_obj
