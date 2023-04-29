from PIL import Image

def get_bit_list(pix_list):
	bit_list = list()
	mask = 1

	for pix in pix_list:
		for i in range(3):
			bit_list.append(pix[i] & mask)
	print(bit_list)
	return bit_list

def get_byte_list(pix_list):
	bit_list = get_bit_list(pix_list)
	byte_list = bytearray()
	new_byte = 0
	cnt = 7

	for bit in bit_list:
		new_byte += bit << cnt
		if cnt == 0:
			print(new_byte)
			byte_list.append(new_byte)
			new_byte = 0
			cnt = 7
		else:
			cnt -= 1
	print(byte_list)
	return byte_list

def decode_image(img):
	pix_list = list(img.getdata())
	byte_list = get_byte_list(pix_list)
	with open("my_file.txt", "wb") as binary_file:
		binary_file.write(bytes(byte_list))

def main():
	img = Image.open('images/test2.png', 'r')
	decode_image(img)

if __name__ == "__main__":
    main()