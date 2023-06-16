from flask import Flask, render_template, request, jsonify
from PIL import Image
import pytesseract
import io
import base64
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    image_data = request.form['image']
    image = Image.open(io.BytesIO(base64.b64decode(image_data)))

    # Perform OCR using pytesseract
    tesseract_output = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    # Process the tesseract output and create Label Studio compatible tasks
    tasks = convert_to_ls(image, tesseract_output, per_level='block_num')

    # Return the tasks as JSON response
    return jsonify(tasks)

def convert_to_ls(image, tesseract_output, per_level='block_num'):
    # Your conversion logic here
    # Convert the OCR output to Label Studio compatible tasks
    # ...

if __name__ == '__main__':
    app.run(debug=True)

