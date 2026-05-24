from flask import Flask
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY', 'parkify-dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///parkify.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import models
from routes import routes
