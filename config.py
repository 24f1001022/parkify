from dotenv import load_dotenv
from os import getenv
load_dotenv()
from app import app
app.config['SECRET_KEY']=getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI']=getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False