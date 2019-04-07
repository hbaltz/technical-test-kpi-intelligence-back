from flask import Flask  # Import the Flask class
from . import config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)    # Create an instance of the class for our use
app.config.from_object(config.Config)
db = SQLAlchemy(app)

from . import models