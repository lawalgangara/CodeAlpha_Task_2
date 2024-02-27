from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Flask-Migrate

from dotenv import load_dotenv
import os

app = Flask(__name__)
app.config.from_object(Config)

# Load environment variables from .env file
load_dotenv()

# Load secret key from environment variable
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Load database URI from environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate

from app.routes.root import *
from app.models.user import *
