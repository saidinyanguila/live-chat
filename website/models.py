from flask_login import UserMixin
import random
from . import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(32))
    user_img_path = db.Column(db.String(255), nullable=False, default="/static/img/default_user.png")

    col_r = db.Column(db.Integer, nullable=False, default=0)
    col_g = db.Column(db.Integer, nullable=False, default=0)
    col_b = db.Column(db.Integer, nullable=False, default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "user_img_path" : self.user_img_path 
        }


