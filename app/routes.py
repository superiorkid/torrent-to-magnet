from app import app
from flask import render_template, request,flash, redirect
import bencodepy
import hashlib
import base64
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = set(['torrent'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            metadata = bencodepy.decode_from_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            subj = metadata[b'info']
            hashcontents = bencodepy.encode(subj)
            digest = hashlib.sha1(hashcontents).digest()
            b32hash = base64.b32encode(digest).decode()
            magnet = 'magnet:?' + 'xt=urn:btih:' + b32hash + '&dn=' + metadata[b'info'][b'name'].decode() + '&tr=' + metadata[b'announce'].decode() + '&xl=' + str(metadata[b'info'][b'piece length'])

            flash('File successfully uploaded')
            return render_template('index.html', magnet=magnet)
        else:
            flash('Allowed file types are torrent only')
            return redirect(request.url)

