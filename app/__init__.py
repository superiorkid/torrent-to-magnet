from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap4

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap4(app)

from app import routes