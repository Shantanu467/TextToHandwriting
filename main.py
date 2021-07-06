from pywhatkit import text_to_handwriting
from PIL import Image

fo = open("D:\\Projects\\python\\TextToHandwriting\\Intro.txt", "r")
str = fo.read()

text_to_handwriting(str, "D:\\Projects\\python\\TextToHandwriting\\output.png", ['0', '0', '0'])

image1 = Image.open(r'D:\\Projects\\python\\TextToHandwriting\\output.png')
im1 = image1.convert('RGB')
im1.save(r'D:\\Projects\\python\\TextToHandwriting\\output.pdf')
