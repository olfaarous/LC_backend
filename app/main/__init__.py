from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name
import os
from pathlib import Path
from flask_cors import CORS

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


cwd = Path.cwd()
UPLOAD_FOLDER = cwd.parent.parent / "uploads"

def create_app(config_name):
    app = Flask(__name__)
    cors = CORS(app)
    app.config.from_object(config_by_name[config_name])
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app