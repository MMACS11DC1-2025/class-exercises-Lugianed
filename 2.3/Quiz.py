tally = 0
print("Put the LETTER(captial) from one of the options given")
# Question 1
print("What is 7 x 3?")
print("A = 3")
print("B = 21")
print("C = 10")
print("D = 20")
answer1 = input("What is the answer? ")

if answer1.upper() == "B":
    print("Correct answer")
    tally = tally + 1
else:
    print("Wrong answer")

print("")
print("")

# Question 2
print("What is 2 % 5?")
print("A = 0")
print("B = 5")
print("C = 2")
print("D = 12")
answer2 = input("What is the answer? ")

if answer2.upper() == "C":
    print("Correct answer")
    tally = tally + 1
else:
    print("Wrong answer")
    
print("")
print("")

# Question 3
print("What is 9 + 10?")
print("A = 19")
print("B = 21")
print("C = 20")
print("D = 17")
answer3 = input("What is the answer? ")

if answer3.upper() == "A":
    print("Correct answer")
    tally = tally + 1
else:
    print("Wrong answer")

print("")
print("")

# Question 4
print("What is 180 % 16?")
print("A = 18")
print("B = 14")
print("C = 20")
print("D = 0")
answer4 = input("What is the answer? ")

if answer4.upper() == "B":
    print("Correct answer")
    tally = tally + 1
else:
    print("Wrong answer")
    
print("")
print("")

# Question 5
print("Who spends the most time on their phone in Computer Science?")
print("A = Gabe")
print("B = Aaryan")
print("C = Greysen")
print("D = Theo")
answer5 = input("What is the answer? ")

if answer5.upper() == "D":
    print("Correct answer")
    tally = tally + 1
else:
    print("Wrong answer")

percent = tally/5 * 100
print("Your score is " + str(tally) +"/5, or " +str(percent) +"%")

    
