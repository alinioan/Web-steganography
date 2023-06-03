from PIL import Image
import argparse

def get_bit_list_from_image(pix_list):
	bit_list = list()
	mask = 1

	for pix in pix_list:
		for i in range(3):
			bit_list.append(pix[i] & mask)
	return bit_list

def get_byte_list(pix_list):
	bit_list = get_bit_list_from_image(pix_list)
	byte_list = bytearray()
	new_byte = 0
	cnt = 7 # counter used to add bits to byte (values from 0 to 7)
	for bit in bit_list:
		new_byte += bit << cnt
		if cnt == 0:
			byte_list.append(new_byte)
			if new_byte == 0: # null string terminator
				return byte_list
			new_byte = 0
			cnt = 7
		else:
			cnt -= 1
	return byte_list

def decode_image(img_name):
	img = Image.open(img_name, 'r')
	pix_list = list(img.getdata())
	byte_list = get_byte_list(pix_list)

	# check if final string is valid
	contains_non_ascii = any(not chr(b).isascii() for b in byte_list)
	if contains_non_ascii:
		text = "Error: The image you provided was not encoded with our encoding algorithm or isn't encoded at all.\nPlease encode an image first or input a vaild image."
	else:
		text = byte_list.decode('utf-8')
		text = str(text)
	return text

def encode_pixels(pixels, ascii_values):
	pixel_pos = 0
	for char in ascii_values:
		cnt = 7
		while cnt >= 0:
			mask = 1 << cnt
			cnt -= 1
			# set pixel bit to 0
			zero_mask = 254 # this is 11111110 in binary
			pixels[pixel_pos] = pixels[pixel_pos] & zero_mask

			# change the bit from the pixel
			if char & mask:
				bit = 1
			else:
				bit = 0
			pixels[pixel_pos] = pixels[pixel_pos] | bit
			pixel_pos += 1
	
	return pixels, pixel_pos

def create_output_image(img, pixels):
	image_out = Image.new(img.mode, img.size)
	pixels_out = list()

	# restore tuples 
	tup = tuple()
	for i in range(0, int(len(pixels)), 3):
		tup = (pixels[i], pixels[i + 1], pixels[i + 2]) 
		pixels_out.append(tup)
	
	image_out.putdata(pixels_out)
	return image_out

def encode_image(img_name, text):
	img = Image.open(img_name, 'r')
	pix_list = list(img.getdata())
	pixels = []
	
	# get pixel list
	for row in pix_list:
		for tup in row:
			pixels.append(tup)
	
	# get ascii values list from input text
	ascii_values = [ord(char) for char in text]
	pixels, encoded_pixels = encode_pixels(pixels, ascii_values)

	# add null string terminator
	if encoded_pixels < len(pixels):
		for i in range(8):
			zero_mask = 254 # this is 11111110 in binary
			pixels[encoded_pixels + i] = pixels[encoded_pixels + i] & zero_mask
	
	image_out = create_output_image(img, pixels)
	image_out.save('static/last_image.png')
	return image_out


def main():
	parser = argparse.ArgumentParser(description="Encode/Decode program")

	subparser = parser.add_subparsers(dest='command')
	encode = subparser.add_parser('encode')
	decode = subparser.add_parser('decode')
	encode.add_argument('--filename', type=str, required=True)
	encode.add_argument('--text', type=str, required=True)

	decode.add_argument('--filename', type=str, required=True)
	args = parser.parse_args()
	if args.command == 'encode':
		encode_image(args.filename, args.text)
	elif args.command == 'decode':
		print(decode_image(args.filename))

if __name__ == "__main__":
	main()
	