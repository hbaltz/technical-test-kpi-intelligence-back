from flask import Flask  # Import the Flask class
from . import config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)    # Create an instance of the class for our use
app.config.from_object(config.Config)
cors = CORS(app)
db = SQLAlchemy(app)

from . import models