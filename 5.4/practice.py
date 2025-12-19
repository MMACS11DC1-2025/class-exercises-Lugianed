from PIL import Image

file = Image.open("5.4/jelly_beans.jpg")
jbimg = file.load()

image_output = Image.open("5.4/jelly_beans.jpg")

width = file.width
height = file.height

for x in range(width):
    for y in range(height):
        r = jbimg[x, y][0]
        g = jbimg[x, y][1]
        b = jbimg[x, y][2]
        
        if 150 < r < 256 and 150 < g < 256 and 0 < b < 150:
            image_output.putpixel((x, y), (255, 255, 255))

image_output.save("jelly_beans_white.png", "png")
