from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_migrate import Migrate


app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config.from_object("config")
db.init_app(app)
db.create_all(app=app)
from zoom_recording_manager import models
from zoom_recording_manager import views
