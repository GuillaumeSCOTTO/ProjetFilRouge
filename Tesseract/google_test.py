from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pytesseract

#config tesseract
custom_config = r"--oem 3 --psm 11 -c tessedit_char_whitelist= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '"

path = '/Users/scotto/PycharmProjects/ProjetFilRouge/test_evolve.jpg'
im = np.array(Image.open(path))
plt.figure(figsize=(10,10))
plt.title('PLAIN IMAGE')
plt.imshow(im); plt.xticks([]); plt.yticks([])
plt.savefig('img1.png')
text = pytesseract.image_to_string(im)
print(text.replace("\n", " "))


def preprocess_final(im):
    im= cv2.bilateralFilter(im,5, 55,60)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    _, im = cv2.threshold(im, 240, 255, 1)
    return im


#img=np.array(Image.open('..\\immagini_test_small\\meme3.jpg'))
im= preprocess_final(im)
text = pytesseract.image_to_string(im, lang='eng', config=custom_config)
print(text.replace("\n", " "))