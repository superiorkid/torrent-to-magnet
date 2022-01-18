from app import app, photos
from flask import render_template
from .forms import UploadForm


@app.post('/')
@app.get('/')
def index():
    form = UploadForm()

    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = photos.url(filename)
    else:
        file_url = None

    return render_template('index.html', form=form, file_url=file_url)