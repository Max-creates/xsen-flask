from flask import Flask, request
import os
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return '🟢 Xsen Flask Server is up and running!'

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No image file', 400

    image = request.files['image']

    if image.filename == '':
        return 'No selected file', 400

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{timestamp}_{image.filename}"
    image.save(os.path.join(UPLOAD_FOLDER, filename))

    return f"Image received and saved as {filename}", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
