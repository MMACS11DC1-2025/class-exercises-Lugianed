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
# Gets those imputs and prints out a fraction score of what we had simular and a message depending on the score


# Opens the file and reads it one line at a time
file = open("2.4/responses.csv")
file.readline()


for i in range(2):
    file.readline()

me = file.readline().strip().split(",")


for line in file:

    digit = input("What is your favourite digit (1-10): ").strip().lower()
    pet = input("What is your favourit pet: ").strip().lower()
    subject = input("What is your favourite subject: ").strip().lower()
    play = input("What is your favourite sport to play: ").strip().lower()
    watch = input("What is your favourite sport to watch: ").strip().lower()
    music = input("What is your favourite music genre: ").strip().lower()
    movie = input("What is your favourite movie genre: ").strip().lower()
    movie = input("What is your favourite movie genre: ").strip().lower()