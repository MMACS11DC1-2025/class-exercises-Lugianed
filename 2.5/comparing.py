"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""

# Opens the file up and reads the line with my information
# Asks the user for their imput on the same questions that I answered
# Gets those imputs and prints out a fraction score of what we had simular

# Example:
# What is your favourite digit (1-10): 6
# What is your favourit pet: FISH
# What is your favourite subject: MaTh
# What is your favourite sport to play: 67
# What is your favourite sport to watch: idk
# What is your favourite music genre: CLASSical
# What is your favourite movie genre: horror
# What is your favourite nearby resturant: KFC
# You chose the same digit as me.
# You chose the same pet as me.
# You chose the same subject as me.
# I didn't understand your answer for your favourite sport to play.
# I didn't understand your answer for your favourite sport to watch.
# You chose the same music genre as me.
# You didn't choose the same movie genre as me.
# You didn't choose the same fast food as me.
# You are 4/8 as same as me.


# Opens the file and reads it one line at a time
file = open("2.4/responses.csv")
file.readline()

score = 0

for i in range(1):
    file.readline()

me = file.readline().strip().split(",")

# Collects data from the user
digit = input("What is your favourite digit (1-10): ").strip().lower()
pet = input("What is your favourit pet: ").strip().lower()
subject = input("What is your favourite subject: ").strip().lower()
play = input("What is your favourite sport to play: ").strip().lower()
watch = input("What is your favourite sport to watch: ").strip().lower()
music = input("What is your favourite music genre: ").strip().lower()
movie = input("What is your favourite movie genre: ").strip().lower()
food = input("What is your favourite nearby resturant: ").strip().lower()

# Checks all the data against mine
if digit == me[2]:
    print("You chose the same digit as me.")
    score += 1
elif digit != me[2]:
    print("You didn't choose the same digit as me.")
else:
    print("I didn't understand your answer for your favourite digit.")

if pet == me[3].lower():
    print("You chose the same pet as me.")
    score += 1
elif pet != me[3].lower():
    print("You didn't choose the same pet as me.")
else:
    print("I didn't understand your answer for your favourite pet to have.")

if subject == me[4].lower():
    print("You chose the same subject as me.")
    score += 1
elif subject != me[4].lower():
    print("You didn't choose the same subject as me.")
else:
    print("I didn't understand your answer for your favourite subject.")

if play == me[5].lower():
    print("You chose the same sport to play as me.")
    score += 1
elif play != me[5].lower():
    print("You didn't choose the same sport to play as me.")
else:
    print("I didn't understand your answer for your favourite sport to play.")

if watch == me[6].lower():
    print("You chose the same sport to watch as me.")
    score += 1
elif watch != me[6].lower():
    print("You didn't choose the same sport to watch as me.")
else:
    print("I didn't understand your answer for your favourite sport to watch.")

if music == me[7].lower():
    print("You chose the same music genre as me.")
    score += 1
elif music != me[7].lower():
    print("You didn't choose the music genre as me.")
else:
    print("I didn't understand your answer for your favourite music genre.")

if movie == me[8].lower():
    print("You chose the same movie genre as me.")
    score += 1
elif movie != me[8].lower():
    print("You didn't choose the same movie genre as me.")
else:
    print("I didn't understand your answer for your favourite movie genre.")

if food == me[9].lower():
    print("You chose the same fast food as me.")
    score += 1
elif food != me[9].lower():
    print("You didn't choose the same fast food as me.")
else:
    print("I didn't understand your answer for your favourite fast food.")

# Prints out the final score
print("You are " + str(score) + "/8 as same as me.")
