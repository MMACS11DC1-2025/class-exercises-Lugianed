"""
Make An Interactive Drawing or Animation 
Explore the turtle drawing package to create an interactive drawing.
It should use a while loop.
Your program should also include at least one function you’ve made yourself 
"""

import turtle
t = turtle.Turtle()

def circle():
  
  t.circle(67)
  

def tri():
	t.forward(100)
	t.left(120)
	t.left(120)
	t.forward(100)
	t.right(120)
	t.forward(100)
	t.penup()
  
 
while True:
  command = input("Do you want a triangle or circle?").lower()
  
  if command == "triangle":
    tri()
    break
  elif command == "circle":
    circle()
    break
  else:
    print("I don't understand")