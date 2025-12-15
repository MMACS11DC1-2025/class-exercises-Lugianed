from PIL import Image
import time

# master list of all pink percentages
picture_percents = []

# checks if it is pink
def is_target_color(r, g, b):
    if r >= 115 and b >= 65 and g <= 185:
        return True
    else:
        return False
    
# masterlist of images
image_list = ("pink1.webp", "pink2.webp", "pink3.webp", "pink4.webp", "pink5.webp",
              "pink6.webp", "pink7.webp", "pink8.webp", "pink9.webp", "pink10.webp")

# start of timing
pixel_analysis_start = time.time()

# goes through each image
for image in image_list:
    file = Image.open("6.7/" + image)
    img = file.load()
    width = file.width
    height = file.height

    # list of pink pixels in current image and restarts for the next
    pink_pixels = []

    # goes through each pixel in the images
    for x in range(width):
        for y in range(height):
            r = img[x, y][0]
            g = img[x, y][1]
            b = img[x, y][2]
            # checks if pink condition is true
            if is_target_color(r, g, b):
                pink_pixels.append((img, (x, y)))

    # calculates percentage of pink pixels
    num_pink = len(pink_pixels)
    total_pixels = width * height
    pink_ratio = num_pink / total_pixels
    pink_percent = pink_ratio * 100
    
    # the thing that user sees
    report = image + " has {:.2f}% pink.".format(pink_percent)
    print(report)

    # adds to master list
    pink_round = round(pink_percent)
    picture_percents.append(pink_round)
# finishes timing
pixel_analysis_end = time.time()
pixel_analysis_time = pixel_analysis_end - pixel_analysis_start
print("Anaylsis through all pixels took {:.3f} seconds to look through.".format(pixel_analysis_time))

# selection sort
for i in range(len(picture_percents)):
    smallest_score = picture_percents[i]
    smallest_index = i
    for j in range(i + 1, len(picture_percents)):
        if picture_percents[j] > smallest_score:
            smallest_score = picture_percents[j]
            smallest_index = j
    # switches to fulfill the list order
    picture_percents[i], picture_percents[smallest_index] = (picture_percents[smallest_index], picture_percents[i])

# binary search (for a list of numbers)
def search(numbers, query):
    search_start_index = 0
    search_end_index = len(numbers) - 1

    while search_start_index <= search_end_index:
        midpoint = (search_start_index + search_end_index) // 2
        if numbers[midpoint] == query:
            return midpoint
        elif numbers[midpoint] > query:
            search_start_index = midpoint + 1
        else:
            search_end_index = midpoint - 1
    return -1

# shows top 5 pinkest pictures
top_5 = picture_percents[:5]
print("The top 5 pinkest pictures have these percentages: " + str(top_5))

# user input to use binary search function
print("Not just these 5 have been put into the list. It is in order from highest to lowest percentage of pink pixels.")
finder = int(input("What percentage would you want to find the place of? "))
results = search(picture_percents, finder) + 1

# checks if in list or not
if search(picture_percents, finder) == -1:
    print("That percentage is not in the list.")
else:
    print("The percentage you wanted to find is in position: " + str(results))