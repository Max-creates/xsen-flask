from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = '/tmp/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return '🟢 Xsen Flask Server is up and running!'

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image file"}), 400

    image = request.files['image']

    if image.filename == '':
        return jsonify({"error": "No selected file"}), 400

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{timestamp}_{image.filename}"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    image.save(filepath)

    return jsonify({"status": "ok", "filename": filename}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

