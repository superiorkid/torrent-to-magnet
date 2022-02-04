from email.mime import base
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SECRET_KEY = 'hard-to-guess'
  UPLOADED_PATH = os.path.join(basedir, 'uploads')

  # flask-dropzone config
  DROPZONE_ALLOWED_FILE_TYPE = '.torrent'
  DROPZONE_MAX_FILE_SIZE = 2
  DROPZONE_ALLOWED_FILE_CUSTOM = True
  DROPZONE_MAX_FILES = 1
  DROPZONE_REDIRECT_VIEW = 'completed'