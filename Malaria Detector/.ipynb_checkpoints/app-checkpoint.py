from flask import Flask, request, render_template
import os
import base64
from keras.models import load_model
from PIL import Image
import numpy as np


app = Flask(__name__)
model = load_model('model/Malaria_Detection.h5')
# Set the directory where uploaded images will be saved
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html', upimg='0')

# Route for image upload
@app.route('/process', methods=['POST'])
def process():

    # Check if the request contains a file
    if 'image_file' not in request.files:
        return 'No file found', 400

    # Get the uploaded file
    img = request.files['image_file']
    img.save(os.path.join(app.config['UPLOAD_FOLDER'], img.filename))
    try:
        
        img2 = Image.open(f"Uploads/{img.filename}")
        img2 = img2.resize((224, 224))  # Resize the image to target size
        img2 = np.array(img2)  # Convert image to numpy array

        # Perform further processing on the loaded image
        img2 = np.expand_dims(img2, axis=0)
        img2 = img2 / 255.0
        predictions = model.predict(img2)
        with open(os.path.join(app.config['UPLOAD_FOLDER'], img.filename), 'rb') as file:
            img2 = file.read()
        dataURL = f"data:jpeg;base64,{base64.b64encode(img2).decode('utf-8')}"
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], img.filename))
        return render_template('index.html', disp=1, detect=int(np.round(predictions)), upimg=dataURL)
    except Exception as ex:
        print(f"Exception Raised: {ex}")
        return render_template('index.html', disp=0, upimg="0")

if __name__ == '__main__':
    app.run(debug=True)