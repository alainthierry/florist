""" 
	Alain Thierry I.M
	27/02/2021

	Image reduce size without comprimizing quality
"""
from PIL import Image
import sys

def main():

	if len(sys.argv) >= 2:
		path = sys.argv[1]
		image = Image.open(path)
		path = "scaled_"+path
		
		image_resized = image.resize((800, 500))
		image_resized.save(path, optimize=True, quality=95)
	else:
		print("Image file was not given !")


if __name__ == '__main__':
	main()
