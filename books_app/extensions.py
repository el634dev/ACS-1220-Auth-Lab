from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from books_app.config import Config
from .models import User
import os

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

###########################
# Authentication
###########################

# Add authentication setup code here!
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

# ------------------------
# User Loader Function
@login_manager.user_loader
def load_user(user_id):
    """
    Desc: Load user with a unique id
    Param: user_id: unique and assign randomly to each user
    Return: user_id
    """
    return User.query.get(user_id)

# (needed so that server will run)
bcrypt = Bcrypt(app)
