from flask import Blueprint, request, flash, redirect
import pandas as pd
import os
import random
from . import db
from .models import User

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=["POST"])
def login():
    print("in login method")
    name = request.form.get('name')
    user_id = request.form.get('user_id')

    if name:
        user = User.query.filter_by(name=name).first()
        return redirect('../templates/topics.html')
    elif user_id:
        print("in user id")


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
