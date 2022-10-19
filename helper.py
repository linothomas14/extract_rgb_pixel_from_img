import numpy as np

# print RGB value per pixel
def printRGBValue(img,height,width):
    for h in range(height):
        for w in range(width):
            pixel_value = img.getpixel((w,h))
            print(pixel_value, end= "")
            
        print()


# print RGB value per pixel
def printHistogram(img,height,width):

    a = np.zeros(shape=(256, 3))
    a = a.astype(int)
    for h in range(height):
        for w in range(width):
            
            pixel_value = img.getpixel((w,h))
            
            for i,val in enumerate(pixel_value):
                a[val,i] += 1

    print("\tR\tG\tB")
    for i,val in enumerate(a):
        
        print('{0}\t{1}\t{2}\t{3}'.format(i,val[0],val[1],val[2]))
        # print(a)