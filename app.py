from steganography import decode_image, encode_image
from flask import Flask, render_template, request, send_file

app = Flask(__name__)
last_decoded_text = None
last_encoded_image = None

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/image/encode', methods=['POST', 'GET'])
def encode():
	global last_encoded_image
	error_message = ''
	header = 'Encoded Image:'
	if request.method == 'POST':
		if 'file' not in request.files:
			error_message='No file uploaded.'
			return render_template('/image/encode.html', header=error_message)
		
		file = request.files['file']
		message = request.form.get('message')

		if file.filename == '':
			return render_template('/image/encode.html', header='Error: No selected file.')
		
		if not message:
			return render_template('/image/encode.html', header='Error: No message provided.')

		encoded_image = encode_image(file, message)

		last_encoded_image = encoded_image

	return render_template('/image/encode.html', header=header, image=last_encoded_image)

@app.route('/image/last/encoded')
def get_last_encoded_image():
	global last_encoded_image
	
	if last_encoded_image is None:
		return 'No encoded image available.'

	return send_file('static/last_image.png')

@app.route('/image/decode', methods=['POST', 'GET'])
def decode():
	header = 'Decoded text:'
	global last_decoded_text
	decoded_text = ""
	if request.method == 'POST':
		if 'file' not in request.files:
			render_template('/image/decode.html', header=header)

		file = request.files['file']
		if file.filename == '':
			return render_template('/image/decode.html', header='Error: No file was selected')

		decoded_text = decode_image(file)

		# Store the decoded message
		last_decoded_text = decoded_text

	return render_template('/image/decode.html', header=header, text=decoded_text)

@app.route('/image/last/decoded')
def get_last_decoded_message():
	global last_decoded_text

	if last_decoded_text is None:
		return 'No decoded data available.'

	return last_decoded_text

@app.route('/about')
def about():
	return render_template('about.html')
	
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
