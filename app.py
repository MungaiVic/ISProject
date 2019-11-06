import os
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_mail import Mail
from flask_security import Security, login_required, SQLAlchemySessionUserDatastore
from werkzeug.utils import secure_filename
from comparison import image_comparison
from config import Config
from database import db_session
from forms import RegistrationForm
from models import User, Role

app = Flask(__name__)
# set up the configurations
app.config.from_object(Config)
# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
security = Security(app, user_datastore, register_form=RegistrationForm)

mail = Mail()
mail.init_app(app)


# renders the home page
@app.route('/')
def home():
    return render_template('home.html')


# renders the about page
@app.route('/about')
def about():
    return render_template('about.html')


# renders the users profile page
@app.route('/profile', methods=['GET'])
def profile():
    # get the user
    # get a user details
    # render a profile page of the user
    return render_template('profile.html')


# Dashboard
@login_required
@app.route('/dashboard')
def dashboard():
    temp = []
    date = "20-4-2000"
    return render_template('dashboard.html', image_names=temp, date=date)


# uploading files
app.config["ALLOWED_EXTENSIONS"] = ['JPG']


# checks if a file is of the allowed extension
def allowed_file(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit('.', 1)[1]
    if ext.upper() in app.config["ALLOWED_EXTENSIONS"]:
        return True
    else:
        return False


@login_required
@app.route('/photographer/uploads', methods=['POST', 'GET'])
def photographer_upload():
    # if request method is post
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files.getlist('file')[0]
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        elif file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_name = file.filename
            flash("Image Uploaded Successfully", "success")

            # inserting file path to the database
            # save the photograph
            flash("Image Uploaded Successfully", "success")
            return redirect(url_for('dashboard'))

        else:
            flash('Allowed file types are .png, .jpg, .jpeg')
            return redirect(request.url)
    # if the request is any other than get
    return render_template('uploads.html')


@login_required
@app.route('/upload', methods=['POST', 'GET'])
def client_upload():
    if request.method == 'POST':
        # check if the post request has any files
        if 'file' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
        file = request.files['file']
        # check if filename is empty
        if file.filename == '':
            flash('No file selected for uploading', 'danger')
            # render the form again
            return redirect(request.url)
        # check if the file type is allowed
        elif allowed_file(file.filename):
            # get the secure filename
            filename = secure_filename(file.filename)
            # get the file path
            file_path = os.path.join(app.config['CLIENT_FOLDER'], filename)
            # save file
            file.save(file_path)

            # get all photos after ranking them
            photos = [object]
            ranked_photos = image_comparison(file_path, photos)
            # map the photos with the photographer and return the photographer name ranked in order of average
            # return list of photographer objects structure {name,link )
            # return a page will all the ranked photos
            return render_template('Comparison.html', photos=ranked_photos, current_photo="Client_Uploads/" + filename)
        # warn user of invalid type
        else:
            flash('Invalid file type', 'danger')
            # render the form again
            return redirect(request.url)
    else:
        return render_template('Comparison.html')


# as a photographer edit a photo
@login_required
@app.route('/edit/<photo_id>', methods=['POST', 'GET'])
def edit(photo_id):
    if request.method == "GET":
        # show the edit photo page
        return redirect('dashboard')
    if request.method == "POST":
        # save the edited images
        pass


# Server Startup
if __name__ == '__main__':
    # debug prevents the one from restarting each time you want to test it
    app.run(debug=True)
