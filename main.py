from PIL import Image 

file_name = "indo.jpg"

img = Image.open(file_name)

img = img.resize((5, 5))

img = img.convert("RGB")

img.save("output.jpg")

width, height = img.size

for h in range(height):
    for w in range(width):
        pixel_value = img.getpixel((w,h))
        print(pixel_value, end= ")")
    print()

