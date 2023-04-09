from . import db


class User(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    date_registered = db.Column(db.Date)


# class Scores(db.Model):
#     id = db.Column(db.Integer, primary_key=True)


# class Subjects(db.Model):
#     subject_id = db.Column(db.Integer, primary_key=True)
#     school_level = db.Column(db.String(30))
#     subject_name = db.Column(db.String(30))
