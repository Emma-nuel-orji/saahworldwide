from app import db, app
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_file = db.Column(db.String(60), nullable=False, default='default.jpg.png')
