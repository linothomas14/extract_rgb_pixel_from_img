from PIL import Image

from helper import printRGBValue, printHistogram

file_name = "mario.jpg"

img = Image.open(file_name)

img = img.resize((100, 100))

img = img.convert("RGB")

width, height = img.size

# assignment week 2
# printRGBValue2(img,height,width)

# assignment week 4
# printRGBValue(img,height,width)
printHistogram(img,height,width)
