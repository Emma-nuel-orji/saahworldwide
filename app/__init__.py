import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import smtplib


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOADED_PHOTO_DEST'] = os.path.join(basedir, 'static/img')
app.config['UPLOAD_FOLDER'] = 'static/img'
app.config['SECRET_KEY'] = '493d18cba56d77f3b1a10af73e21af17'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Emmanuel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
EMAIL_USERNAME = "eorji452@gmail.com"
EMAIL_HOST_PASSWORD = "sqokdetbwukuwxzo"
app.config['MAIL_USERNAME'] = EMAIL_USERNAME
app.config['MAIL_PASSWORD'] = EMAIL_HOST_PASSWORD

mail = Mail(app)
db = SQLAlchemy(app)

from app.users.routes import users

app.register_blueprint(users)
