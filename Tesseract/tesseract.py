from PIL import Image
import pytesseract
import os
import imghdr
import cv2
import numpy as np


def process_image(iamge_name, lang_code): return pytesseract.image_to_string(Image.open(iamge_name), lang=lang_code)

def process_image2(image):
	custom_config = r"--oem 3 --psm 11 -c tessedit_char_whitelist= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '"
	text = pytesseract.image_to_string(image, lang='eng', config=custom_config)
	text = text.replace("\n"," ")
	print(text)
	return text

def print_data(data): print(data)

def output_file(f,texte_path,data):
	path = texte_path + f+".txt"
	#print(path)
	file = open(path, "w")
	#file = open(filename, "w+")
	file.write(data)
	file.close()


def preprocess_final(im):
    im= cv2.bilateralFilter(im,5, 55,60)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    _, im = cv2.threshold(im, 240, 255, 1)
    return im

def main():
	directory = './images'
	textes_path = './textes/'
	#textes_path2 = '/Users/scotto/PycharmProjects/ProjetFilRouge/textes2/'
	for filename in os.listdir(directory):
		f = os.path.join(directory, filename)
		# checking if it is a file
		if os.path.isfile(f):
			# checking if it is an image
			if imghdr.what(f):
				im = np.array(Image.open(f))
				im = preprocess_final(im)
				text = process_image2(im)
				#image = process_image(f, "eng")
				output_file(filename,textes_path,text)


if  __name__ == '__main__':
	main()


