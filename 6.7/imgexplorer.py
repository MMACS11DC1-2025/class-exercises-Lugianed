from PIL import Image
import time

pink_color = 0

image_list = ("pinkflower1.webp", "pinkflower2.webp", "pinkflower3.webp", "pinkflower4.webp", "pinkflower5.webp",
              "pinkflower6.webp", "pinkflower7.webp", "pinkflower8.webp", "pinkflower9.webp", "pinkflower10.webp")
for image in image_list:
    file = Image.open("6.7/" + image)
    img = file.load()

    width = file.width
    height = file.height

    def is_target_color(r, g, b):
        if 100 <= r >= 255 and 7 <= g >= 150 and 120 <= b >= 200:
            return True
        return False
    for x in range(width):
        for y in range(height):
            r = img[x, y][0]
            g = img[x, y][1]
            b = img[x, y][2]
        if is_target_color(r, g, b):
            pink_color += 1

print("Number of images with pink color:", pink_color)