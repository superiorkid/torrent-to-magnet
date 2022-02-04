from app import app
from flask import render_template, request
import bencodepy
import hashlib
import base64
import os

@app.route('/', methods=['POST', 'GET'] )
def make_torrent_to_magnet():
  if request.method == "POST":
    f = request.files.get('file')
    file_path = os.path.join(app.config['UPLOADED_PATH'], f.filename)
    f.save(file_path)
    
    metadata = bencodepy.decode_from_file(file_path)
    subj = metadata[b'info']
    hashcontents = bencodepy.encode(subj)
    digest = hashlib.sha1(hashcontents).digest()
    b32hash = base64.b32encode(digest).decode()
    magnet = 'magnet:?' + 'xt=urn:btih:' + b32hash + '&dn=' + metadata[b'info'][b'name'].decode() + '&tr=' + metadata[b'announce'].decode() + '&xl=' + str(metadata[b'info'][b'piece length'])

    return render_template('index.html', magnet=magnet)
    
  return render_template('index.html')