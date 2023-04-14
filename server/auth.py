from flask import Blueprint, request, flash, redirect, render_template, url_for
import pandas as pd
import os
import random
import re
from . import db, login_manager
from flask_login import login_user, current_user, logout_user
from .models import User
from werkzeug.security import generate_password_hash

auth = Blueprint("auth", __name__)
email_regex = re.compile(
    r"(^[\w.!#$%&'*+/=?^_`{|}~-]+" r"@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$)"
)


@auth.route("/login", methods=["POST"])
def login():
    print("in login method")
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()
    if user is not None and user.check_password(password):
        login_user(user)

        return redirect(url_for("main.topics")), 200

    flash("Invalid email address or password.")

    return "invalid", 400


@auth.route("/register", methods=["POST"])
def register_user():
    # Retrieve the form inputs and perform input validation
    valid_email = is_valid_email(request.form.get("email"))

    # Check if email already exists
    user_check = User.query.filter_by(email=request.form.get("email")).first()
    print(request.form)
    print(user_check)

    # Check if passwords match
    pw_match = request.form.get("password") == request.form.get("passwordcfm")

    # Exit if email or passwords not valid
    if not valid_email or not pw_match or user_check:
        message = ""
        if not valid_email:
            message += "Email format invalid. "
        if not pw_match:
            message += "Passwords don't match. "
        if user_check:
            message += "User with matching email already exists. "

        return f"User not created, {message}", 400

    else:  # Insert into DB
        user = User(
            email=request.form.get("email"),
            firstname=request.form.get("firstname"),
            lastname=request.form.get("lastname"),
            ed_level=request.form.get("ed_level"),
        )
        user.set_password(request.form.get("password"))

        db.session.add(user)
        db.session.commit()

        return "User successfully created", 201


def is_valid_email(email):
    if email_regex.match(email):
        return True
    else:
        return False


# @auth.route("/login", methods=["POST"])
# def start():
#     if request.method == "POST":
#         check_user_data_exists()
#         user_data = pd.read_csv('user_data.csv')

#         # Check if it is a log in or sign up request
#         login_request = False
#         if request.json.get('user_id'):
#             login_request = True

#         if login_request:
#             user_id_exists, user_info_dict = login_request_handler(
#                 request.json.get('user_id'), user_data)
#         elif not login_request and request.json.get('name'):
#             user_id_exists, user_info_dict = register_request_handler(
#                 request.json.get('name'), user_data)
#         else:
#             user_id_exists = False
#             user_info_dict = {
#                 "name": "",
#                 "user_id": "",
#             }

#         resp = {
#             "name": user_info_dict['name'],
#             "user_id": user_info_dict['user_id'],
#             "user_id_exists": user_id_exists
#         }
#         return resp

#     return "Hello world"


# def check_user_data_exists():
#     if not os.path.exists('user_data.csv'):
#         data = {
#             "name": [],
#             "user_id": [],
#             "questions_correct": [],
#             "questions_attempted": []
#         }
#         user_data = pd.DataFrame(data, index=None)
#         user_data.to_csv("user_data.csv", index=None)

#         return True

#     return False


# def login_request_handler(user_id, user_data_file: pd.DataFrame):
#     # Check if it exists within the file
#     user_id_exists = False
#     user_info_dict = {"name": "", "user_id": ""}
#     # To add input validation
#     if len(user_data_file.loc[user_data_file['user_id'] == int(user_id)]) > 0:
#         user_id_exists = True
#         user_info_dict = {
#             "name": user_data_file.loc[user_data_file['user_id'] == int(user_id), 'name'].iloc[0],
#             "user_id": user_id
#         }

#     return user_id_exists, user_info_dict


# def register_request_handler(name, user_data_file):
#     # Generate a user id
#     random_user_id = random.randint(1000, 9999)
#     while random_user_id in user_data_file['user_id']:
#         random_user_id = random.randint(1000, 9999)

#     # Write the user info into the dataframe
#     user_info_dict = {
#         "name": name,
#         "user_id": random_user_id,
#         "questions_correct": 0,
#         "questions_attempted": 0
#     }

#     user_data_file.loc[len(user_data_file)] = [
#         item for item in user_info_dict.values()]
#     user_data_file.to_csv('user_data.csv', index=None)

#     return True, user_info_dict
