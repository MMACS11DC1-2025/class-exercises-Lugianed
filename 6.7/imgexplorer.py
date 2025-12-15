from PIL import Image
import time

picture_percents = []
def is_target_color(r, g, b): # checks if it is pink
    if 150 <= r >= 220 and 20 <= g >= 90 and 100 <= b >= 180:
        return True
    return False
image_list = ("pink1.webp", "pink2.webp", "pink3.webp", "pink4.webp", "pink5.webp",
              "pink6.webp", "pink7.webp", "pink8.webp", "pink9.webp", "pink10.webp")
for image in image_list:
    file = Image.open("6.7/" + image)
    img = file.load()

    width = file.width
    height = file.height
    pink_pixels = []
    for x in range(width):
        for y in range(height):
            r = img[x, y][0]
            g = img[x, y][1]
            b = img[x, y][2]
            if is_target_color(r, g, b):
                pink_pixels.append((img, (x, y)))
    # calculates percentage of pink pixels
    num_pink = len(pink_pixels)
    total_pixels = width*height
    pink_ratio = num_pink / total_pixels
    pink_percent = pink_ratio * 100
    report = (image) + " Is {:.2f}% pink.".format(pink_percent)
    print(report)
    pink_round = round(pink_percent)
    picture_percents.append(pink_round)

# selection sort
for i in range(len(pink_round)):
    smallest_score = pink_round[i]
    smallest_index = i

    for j in range(i+1, len(pink_round)):
        if pink_round[j] < smallest_score:
            smallest_score < pink_round[j]
            smallest_index = j
            pink_round[smallest_index], pink_round[i] = pink_round[i], pink_round[smallest_index]
print(pink_round)

# binary search
def search(list_of_lists, query):
    search_start_index = 0
    search_end_index = len(list_of_lists) - 1
    while search_start_index <= search_end_index:
        midpoint = int((search_start_index + search_end_index) / 2)
        if list_of_lists[midpoint][0] == query:
            return list_of_lists[midpoint][1]
        elif list_of_lists[midpoint][0] < query:
            search_start_index = midpoint + 1
        else:
            search_end_index = midpoint - 1
    return -1
