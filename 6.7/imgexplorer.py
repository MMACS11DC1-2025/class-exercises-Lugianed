from PIL import Image
import time

count = 0
final = 0
def is_target_color(r, g, b):
    if 90 <= r >= 255 and 7 <= g >= 150 and 120 <= b >= 200:
        print(r, g, b)
        return True
    return False
def is_another_color(r, g, b):
    if 3 <= r >= 155 and 5 <= g >= 180 and 0 <= b >= 60:
        print(r, g, b)
        return True
    return False
image_list = ("pinkflower1.webp", "pinkflower2.webp", "pinkflower3.webp", "pinkflower11.jpg", "pinkflower5.webp",
              "pinkflower6.webp", "pinkflower7.webp", "pinkflower8.png", "pinkflower9.png", "pinkflower10.png")
for image in image_list:
    file = Image.open("6.7/" + image)
    img = file.load()

    width = file.width
    height = file.height
    pink_color = 0
    for x in range(width):
        for y in range(height):
            r = img[x, y][0]
            g = img[x, y][1]
            b = img[x, y][2]
            if is_target_color(r, g, b) and is_another_color(r, g, b):
                pink_color += 1
                print(x, y)
                print(image)
        if pink_color == 1:
            final += 1
            break
print(final)