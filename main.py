from PIL import Image

from helper import printRGBValue, printRGBValue2

file_name = "indo.jpg"

img = Image.open(file_name)

img = img.resize((10, 10))

img = img.convert("RGB")

img.save("output.jpg")

width, height = img.size

# assignment week 2
# printRGBValue2(img,height,width)

# assignment week 4
# printRGBValue(img,height,width)
printRGBValue2(img,height,width)
