from . import db, func
import datetime
import pytz
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# To add new DB entry:
# from .models import <Table>
# new_user = <Table>(fields=values)
# db.session.add(new_user)
# db.session.commit()


class User(UserMixin, db.Model):
    current_dt = datetime.datetime.utcnow()
    tz = pytz.timezone("Asia/Singapore")
    now_singapore = tz.fromutc(current_dt).strftime("%Y-%m-%d %H:%M:%S")
    now_singapore = datetime.datetime.now(tz)  # .strftime("%Y-%m-%d %H:%M:%S")
    print(now_singapore)

    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    ed_level = db.Column(db.String(10), nullable=False)
    date_registered = db.Column(db.DateTime, default=now_singapore)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"Email: {self.email}, First Name: {self.firstname}, ID: {self.id}"


class Topics(db.Model):
    subject_id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, nullable=False)
    topic_name = db.Column(db.String(20), nullable=False)


class Subjects(db.Model):
    subject_id = db.Column(db.Integer, primary_key=True)
    subject_level = db.Column(db.String(10))
    subject_name = db.Column(db.String(30))


class Scores(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, primary_key=True)
    attempted = db.Column(db.Integer)
    correct = db.Column(db.Integer)


class QuestionBank(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, primary_key=True)
    difficulty = db.Column(db.Integer)
    question = db.Column(db.Text)
    options = db.Column(db.Text)
    solution = db.Column(db.Text)
