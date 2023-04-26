from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import os
from werkzeug.utils import secure_filename
from stegnography import Stegnography


app = Flask(__name__)

app.secret_key = "secret key"


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# . is current dir
app.config["UPLOAD_FOLDER"] = os.path.join('static', 'images')
app.config["ENCRYPT_UPLOAD_FOLDER"] = os.path.join('static', 'encrypt_images')

# Create upload folder if not exists
if not os.path.exists(app.config["ENCRYPT_UPLOAD_FOLDER"]):
    os.makedirs(app.config["ENCRYPT_UPLOAD_FOLDER"])
if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/upload')
def view_html():
    return render_template('index.html')

@app.route('/encoded_image', methods=['POST', 'GET'])
def encode_file():
    if request.method == 'POST':
        file = request.files['file']
        msg = request.form.get('textmsg')

        if file and msg:
            # get filename and secure it
            original_filename = secure_filename(request.files['file'].filename)
            
            # getting file and saving it to ensure that there is no error in file during processing
            file = request.files['file']
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], original_filename))

            #getting encoded image and saving it png ext.
            encoded_image = Stegnography.encoding(file, msg)
            encoded_filename = f"enc_{os.path.splitext(original_filename)[0]}.png"
            
            #saving encoding file
            encoded_image.save(os.path.join(app.config['ENCRYPT_UPLOAD_FOLDER'], encoded_filename))
            
            # ensuring correct path
            encoded_filename = 'encrypt_images/'+encoded_filename
            original_filename = 'images/'+original_filename
            
            return render_template('show.html', original_filename=original_filename, encoded_filename=encoded_filename)
        return render_template('filerror.html')  #todo
    else:
        flash("Go to /upload to perform encryption first.", 'error')
        return render_template('error.html')
    
@app.route('/decoding', methods=['POST', 'GET'])
def decoding_image():
    if request.method =="POST":
        file = request.files['decodefile']
        if file:
            #getting uploaded file and saving it.
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

            #getting message back
            message = Stegnography.decoding(file)

            return render_template('decode.html', message=str(message))
    else:
        flash("Go to /upload first to upload an image first.", 'error')
        return render_template('error.html')
    
