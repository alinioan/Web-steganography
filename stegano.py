from decode import decode_image
from PIL import Image
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
	uploaded_file = request.files['file']
	uploaded_file.save(uploaded_file.filename)
	
	img = Image.open(uploaded_file.filename, 'r')	
	decode_image(img)
	return 'File uploaded successfully!'

if __name__ == '__main__':
	app.run(debug=True)
