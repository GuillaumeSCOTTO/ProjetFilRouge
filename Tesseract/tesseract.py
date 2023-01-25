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
	path = texte_path + "texte.txt"
	#print(path)
	file = open(path, "a+")
	#file = open(filename, "w+")
	file.write(data)
	file.write("\n \n")
	file.close()


def preprocess_final(im):
    im= cv2.bilateralFilter(im,5, 55,60)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    _, im = cv2.threshold(im, 240, 255, 1)
    return im

def main():
	directory = './images'
	textes_path = './textes/'
	path = textes_path + "texte.txt"
	file = open(path, "w")
	file.close()
	#textes_path2 = '/Users/scotto/PycharmProjects/ProjetFilRouge/textes2/'
	for root, dirs, files in os.walk("."):
		path = root.split(os.sep)
		print((len(path) - 1) * '---', os.path.basename(root))
		for file in files:
			print(len(path) * '---', file)
			f = root+"/"+file
			# checking if it is a file
			if os.path.isfile(f):
				# checking if it is an image
				if imghdr.what(f):
					im = cv2.imread(f)
					#im = np.array(Image.open(f))
					im = preprocess_final(im)
					text = process_image2(im)
					#image = process_image(f, "eng")
					output_file(f,textes_path,text)


if  __name__ == '__main__':
	main()


