from steganography import decode_image, encode_image
from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode')
def encode():
    return render_template('/image/encode.html')

@app.route('/image/last/encoded')
def get_last_encoded_image():
   return "last encode"

@app.route('/image/decode')
def decode():
    return render_template('/image/decode.html')

@app.route('/image/last/decoded')
def get_last_decoded_message():
    return "last dencode"

@app.route('/about')
def about():
    return render_template('about.html')
    
if __name__ == "__main__":
	app.run(debug=True)
