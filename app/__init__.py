from flask import Flask
from config import Config
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class


app = Flask(__name__)
app.config.from_object(Config)
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

from app import routes