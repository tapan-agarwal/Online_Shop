from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect

app = Flask(__name__, template_folder="templates", instance_relative_config=False, static_folder="static")
app.config['SECRET_KEY'] = 'verysecretcode'
app.config['TESTING'] = True
app.config['DEBUG'] = True
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://c1923070:Pinecone318@csmysql.cs.cf.ac.uk:3306/c1923070_team24"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
csrf = CSRFProtect(app)

app.testing = True
    
from app import routes
from .auth import routes

db.create_all()