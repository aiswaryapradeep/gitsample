import typer
import glob
from PIL import Image

img_path ='C:\Users\HP\Desktop\imgto\IMG-20210414-WA0101.jpg'

im = Image.open(img_path)
print('{}'.format(im.format))
print('size: {}'.format(im.size))
print('image mode: {}'.format(im.mode))
im.show()

