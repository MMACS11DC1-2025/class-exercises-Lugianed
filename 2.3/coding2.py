"""
Write an Olympic Judging program that outputs the average scores from 5 different judges. 

Each score is out of 10 points maximum. Half points are allowed (e.g. 7.5)

The program should take 5 inputs and output the final average score.

Example:

Judge 1: 5.5
Judge 2: 10
Judge 3: 7
Judge 4: 8.5
Judge 5: 9
Your Olympic score is 8.0
"""

print("What do you rate them")
jone = float(input("Judge 1: "))
jtwo = float(input("Judge 2: "))
jthree = float(input("Judge 3: "))
jfour = float(input("Judge 4: "))
jfive = float(input("Judge 5: "))

final = (jone + jtwo + jthree + jfour + jfive) / 5
print("Your final score is " + str(final))