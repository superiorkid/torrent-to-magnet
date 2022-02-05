import os

basedir = os.getcwd()

class Config(object):
  SECRET_KEY = 'very-hard-to-guess'
  UPLOAD_FOLDER = os.path.join(basedir, 'uploads')

  if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
