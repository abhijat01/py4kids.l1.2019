import numpy as np

from PIL import Image, ImageDraw, ImageFont
img = Image. new('L', (40, 40))
font = ImageFont.truetype("arial.ttf", 20)
drawer = ImageDraw.Draw(img)
drawer.text((12,8), "H", fill=(255), font=font)
img.save("hello.png")





