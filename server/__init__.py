from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# class User(db.Model):
#     __tablename__ = "Users"
#     _id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30))
#     date_registered = db.Column(db.Date)

#     def __init__(self, name, date_registered):
#         self.name = name
#         self.date_registered = date_registered


def create_app():

    app_obj = Flask(__name__, template_folder='../templates',
                    static_folder='../static')
    app_obj.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    db.init_app(app_obj)

    # Blueprint for auth routes in app
    from .auth import auth as auth_blueprint
    app_obj.register_blueprint(auth_blueprint)

    # Blueprint for non-auth routes in app
    from .app import main as app_blueprint
    app_obj.register_blueprint(app_blueprint)

    with app_obj.app_context():
        db.create_all()

    return app_obj
