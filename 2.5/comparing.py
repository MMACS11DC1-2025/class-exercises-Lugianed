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


# Opens the file and reads it one line at a time
file = open("2.4/responses.csv")
file.readline()

score = 0

for i in range(1):
    file.readline()

me = file.readline().strip().split(",")

digit = input("What is your favourite digit (1-10): ").strip().lower()
pet = input("What is your favourit pet: ").strip().lower()
subject = input("What is your favourite subject: ").strip().lower()
play = input("What is your favourite sport to play: ").strip().lower()
watch = input("What is your favourite sport to watch: ").strip().lower()
music = input("What is your favourite music genre: ").strip().lower()
movie = input("What is your favourite movie genre: ").strip().lower()
food = input("What is your favourite nearby resturant: ").strip().lower()

if digit == me[2]:
    print("You chose the same digit as me.")
    score += 1
elif digit != me[2]:
    print("You didn't choose the same digit as me.")

if pet == me[3].lower():
    print("You chose the same pet as me.")
    score += 1
elif pet != me[3].lower():
    print("You didn't choose the same pet as me.")

if subject == me[4].lower():
    print("You chose the same subject as me.")
    score += 1
elif subject != me[4].lower():
    print("You didn't choose the same subject as me.")

if play == me[5].lower():
    print("You chose the same sport to play as me.")
    score += 1
elif play != me[5].lower():
    print("You didn't choose the same sport to play as me.")

if watch == me[6].lower():
    print("You chose the same sport to watch as me.")
    score += 1
elif watch != me[6].lower():
    print("You didn't choose the same sport to watch as me.")

if music == me[7].lower():
    print("You chose the same music genre as me.")
    score += 1
elif music != me[7].lower():
    print("You didn't choose the music genre as me.")

if movie == me[8].lower():
    print("You chose the same movie genre as me.")
    score += 1
elif movie != me[8].lower():
    print("You didn't choose the same movie genre as me.")

if food == me[9].lower():
    print("You chose the same fast food as me.")
    score += 1
elif watch != me[9].lower():
    print("You didn't choose the same fast food as me.")

print("You are " + str(score) + "/8 as same as me.")
