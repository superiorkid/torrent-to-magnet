from flask import Flask
from config import Config
from flask_dropzone import Dropzone

app = Flask(__name__)
app.config.from_object(Config)
dropzone = Dropzone(app)

from app import routes