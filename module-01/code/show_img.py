import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

def make_image(char, file_name):

    img = Image. new('L', (40, 40))
    font = ImageFont.truetype("arial.ttf", 20)
    drawer = ImageDraw.Draw(img)
    drawer.text((12,8), char, fill=(255), font=font)
    img.save(file_name)

def read_image(file_name):
    im_frame = Image.open(file_name)
    img_data = np.array(im_frame)
    print("Loaded data from file:{}. dimensions of imaged data:{}".format(file_name, img_data.shape))
    return img_data


def png_to_ascii(img_data):
    x,y = img_data.shape
    for i in range(x):
        for j in range(y):
            d = img_data[i,j]
            if d>0:
                d = 1
                img_data[i,j] = 255
            print(d, end="")
        print()
    return img_data


x,y = data.shape
for i in range(x):
    for j in range(y):
        d = data[i,j]
        if d>0:
            d = 1
            data[i,j] = 255
        print(d, end="")
    print()

img = Image.fromarray(data)
img.save("clear.png")

plt.plot(data[20,:])
plt.show()