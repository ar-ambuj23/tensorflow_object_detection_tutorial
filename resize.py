### Image Resizer ###

"""
This script resizes all the jpeg, jpg and png images present in a directory.
The images are resized to 300x300 using PIL.
The images are also renamed to numerical values for better usage.

Usage:
Place the script in the directory containing the images and run it.
OR
Change the dir_path to the image directory and run the srcipt from anywhere.
""" 

from PIL import Image
import os

# To be used when script is placed in the image directory
dir_path = os.getcwd()

# To be used when script is to run from anywhere else
# dir_path = 'PATH_TO_YOUR_IMAGE_DIRECTORY'

for num,image_file_name in enumerate(os.listdir(dir_path)):
	if image_file_name.endswith((".png",".jpg",".jpeg")):
		im = Image.open(image_file_name)
		im = im.resize((300,300),Image.ANTIALIAS)
		im.save(image_file_name)
