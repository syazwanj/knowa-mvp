from flask import (
    Flask,
    request,
    render_template,
    Blueprint,
    send_file,
    url_for,
    redirect,
)
from flask_cors import CORS, cross_origin
from flask_login import login_required, current_user, logout_user
import random
import os
import pandas as pd
from . import db, login_manager
from .models import User

print(__name__)
main = Blueprint("main", __name__)
# bp = Blueprint('node', static_url_path="../node_modules")
# main = Flask(__name__, template_folder="../templates")
# main.config['TEMPLATES_AUTO_RELOAD'] = True
# main.jinja_env.auto_reload = True
# cors = CORS(app, resources={r"/*": {"origins": "*"}})
# app.config['CORS_HEADERS'] = "Content-Type"

# Home API route


@main.route("/")
def demo():
    print("hello world")
    return render_template("index.html")


@main.route("/signin")
def siginin():
    # Check if logged in
    if current_user.is_authenticated:
        return redirect(url_for("main.topics"))
    return render_template("signin.html")


@main.route("/topics")
@login_required
def topics():
    return render_template("topics.html")


@main.route("/questions")
def questions():
    return render_template("questions.html")


@main.route("/register", methods=["GET"])
def register():
    if current_user.is_authenticated:
        logout_user()
    return render_template("registration.html")


@main.route("/login", methods=["POST"])
def start():
    if request.method == "POST":
        check_user_data_exists()
        user_data = pd.read_csv("user_data.csv")

        # Check if it is a log in or sign up request
        login_request = False
        if request.json.get("user_id"):
            login_request = True

        if login_request:
            user_id_exists, user_info_dict = login_request_handler(
                request.json.get("user_id"), user_data
            )
        elif not login_request and request.json.get("name"):
            user_id_exists, user_info_dict = register_request_handler(
                request.json.get("name"), user_data
            )
        else:
            user_id_exists = False
            user_info_dict = {
                "name": "",
                "user_id": "",
            }

        resp = {
            "name": user_info_dict["name"],
            "user_id": user_info_dict["user_id"],
            "user_id_exists": user_id_exists,
        }
        return resp

    return "Hello world"


def check_user_data_exists():
    if not os.path.exists("user_data.csv"):
        data = {
            "name": [],
            "user_id": [],
            "questions_correct": [],
            "questions_attempted": [],
        }
        user_data = pd.DataFrame(data, index=None)
        user_data.to_csv("user_data.csv", index=None)

        return True

    return False


def login_request_handler(user_id, user_data_file: pd.DataFrame):
    # Check if it exists within the file
    user_id_exists = False
    user_info_dict = {"name": "", "user_id": ""}
    # To add input validation
    if len(user_data_file.loc[user_data_file["user_id"] == int(user_id)]) > 0:
        user_id_exists = True
        user_info_dict = {
            "name": user_data_file.loc[
                user_data_file["user_id"] == int(user_id), "name"
            ].iloc[0],
            "user_id": user_id,
        }

    return user_id_exists, user_info_dict


def register_request_handler(name, user_data_file):
    # Generate a user id
    random_user_id = random.randint(1000, 9999)
    while random_user_id in user_data_file["user_id"]:
        random_user_id = random.randint(1000, 9999)

    # Write the user info into the dataframe
    user_info_dict = {
        "name": name,
        "user_id": random_user_id,
        "questions_correct": 0,
        "questions_attempted": 0,
    }

    user_data_file.loc[len(user_data_file)] = [item for item in user_info_dict.values()]
    user_data_file.to_csv("user_data.csv", index=None)

    return True, user_info_dict


@login_manager.user_loader
def load_user(user_id):
    u = User.query.filter_by(id=user_id).first()
    return u


if __name__ == "__main__":
    # from . import db, create_app, models
    # db.create_all(app=create_app())
    main.run(debug=True, port=5000)
