# Drawing different shapes based on user input: pumpkin, snowflake, or tree

import turtle

choice = input("Do you want pumpkin, snowflake, or a tree?").lower()
  
wn = turtle.Screen()
wn.bgcolor("lightblue")

t = turtle.Turtle()
t.speed(100)
t.hideturtle()
# Pumpkin drawing functions

def drawcircle(x,y):
  t.color("orangered")
  t.penup()
  t.goto(x,y)
  t.begin_fill()
  t.circle(70)
  t.end_fill()
# Triangle function for eyes and nose

def triangle(x,y):
  t.color("black")
  t.penup()
  t.goto(x,y)
  t.begin_fill()
  for i in range(3):
  	t.forward(40)
	  t.left(360/3)
  t.end_fill()
# Mouth function

def mouth():
  t.color("black")
  t.up()
  t.goto(-60,40)
  t.down()
  t.begin_fill()
  t.goto(-30,20)
  t.goto(30,20)
  t.goto(60,40)
  t.goto(0,30)
  t.end_fill()
# Stem function

def stem():
  t.color("green")
  t.up()
  t.goto(-40,130)
  t.down()
  t.begin_fill()
  t.goto(40,130)
  t.goto(20,150)
  t.goto(10,170)
  t.goto(0, 180)
  t.goto(-15,175)
  t.goto(-10,155)
  t.goto(-15,140)
  t.goto(-40,130)
  t.end_fill()

# Draw pumpkin if chosen
if choice == "pumpkin":
  drawcircle(20,0)
  drawcircle(-20,0)
  triangle(15,80)
  triangle(-55,80)
  triangle(-20,50)
  mouth()
  stem()
# Refer to pumpkin.png for visual reference

# Snowflake drawing function
t.pencolor("white")
t.speed(67)
t.hideturtle()
true = None
# Recursive snowflake function
def snowflake(size):
  for i in range(6):
    t.forward(size)
    if (size>6):
      snowflake(size/3)
    t.backward(size)
    t.right(60)
# Draw snowflake if chosen
if choice == "snowflake":
  snowflake(150)
# Refer to snowflake.png for visual reference

# Tree drawing function
leaves = input("What season do you want?").lower()

# Dictionary for different leaf colors based on season
seasons = {"summer": "#154734", "spring": "#90ee90", 
           "fall": "#ff4500", "winter": "#ffffff"}

if leaves == "summer":
  def drawTree(level, branchLength):
    if level > 0:
      t.forward(branchLength)
      t.left(40)
      drawTree(level-1, branchLength/1.61)

      t.right(80)
      drawTree(level-1, branchLength/1.61)

      t.left(40)
      t.back(branchLength)
    else:
      t.color(seasons["summer"])
      t.stamp()
      t.color("brown")
  # Position turtle for tree drawing
  t.speed(0)
  t.penup()
  t.goto(0, -180)
  t.left(90)
  t.pendown()
  t.color("brown")
  t.width(3)
  t.shape("triangle")
  # Draw tree if chosen
  # Refer to summer tree with 5 branches.png for visual reference
  if choice == "tree":
    levels = input("Amount of branches(1 and 2 is too low. 3-7 recommended to avoid crashing): ")
    drawTree(int(levels), 120)

if leaves == "spring":
  def drawTree(level, branchLength):
    if level > 0:
      t.forward(branchLength)
      t.left(40)
      drawTree(level-1, branchLength/1.61)

      t.right(80)
      drawTree(level-1, branchLength/1.61)

      t.left(40)
      t.back(branchLength)
    else:
      t.color(seasons["spring"])
      t.stamp()
      t.color("brown")
  # Position turtle for tree drawing
  t.speed(0)
  t.penup()
  t.goto(0, -180)
  t.left(90)
  t.pendown()
  t.color("brown")
  t.width(3)
  t.shape("triangle")

  # Draw tree if chosen
  # Refer to spring tree with 5 branches.png for visual reference
  if choice == "tree":
    levels = input("Amount of branches(1 and 2 is too low. 3-7 recommended to avoid crashing): ")
    drawTree(int(levels), 120)
    
if leaves == "fall" or leaves == "autumn":
  def drawTree(level, branchLength):
    if level > 0:
      t.forward(branchLength)
      t.left(40)
      drawTree(level-1, branchLength/1.61)

      t.right(80)
      drawTree(level-1, branchLength/1.61)

      t.left(40)
      t.back(branchLength)
    else:
      t.color(seasons["fall"])
      t.stamp()
      t.color("brown")
  # Position turtle for tree drawing
  t.speed(0)
  t.penup()
  t.goto(0, -180)
  t.left(90)
  t.pendown()
  t.color("brown")
  t.width(3)
  t.shape("triangle")

  # Draw tree if chosen
  # Refer to fall tree with 5 branches.png for visual reference
  if choice == "tree":
    levels = input("Amount of branches(1 and 2 is too low. 3-7 recommended to avoid crashing): ")
    drawTree(int(levels), 120)
    
if leaves == "winter":
  def drawTree(level, branchLength):
    if level > 0:
      t.forward(branchLength)
      t.left(40)
      drawTree(level-1, branchLength/1.61)

      t.right(80)
      drawTree(level-1, branchLength/1.61)

      t.left(40)
      t.back(branchLength)
    else:
      t.color(seasons["winter"])
      t.stamp()
      t.color("brown")
  # Position turtle for tree drawing
  t.speed(0)
  t.penup()
  t.goto(0, -180)
  t.left(90)
  t.pendown()
  t.color("brown")
  t.width(3)
  t.shape("triangle")
  # Draw tree if chosen
  # Refer to winter tree with 5 branches.png for visual reference
  if choice == "tree":
    levels = input("Amount of branches(1 and 2 is too low. 3-7 recommended to avoid crashing): ")
    drawTree(int(levels), 120)
  # Finish drawing
  turtle.done()
'''''
Testing Log:
  Pumpkin is slightly off center but looks good
  Snowflake is drawn very slowly, increasing the speed
  Tree is hard to implement with the others
  Asking for the amount of branches is causing issues when tree isn't chosen
  Finally got

'''''

'''''
Recursive approach for the tree:
  keeps dividing the size of the branches so it visably looks smaller each time it branches out

Input:
  pumpkin
Output:
  *prints pumpkin drawing*
Input:
  snowflake
Output:
  *prints snowflake drawing*
Input:
  tree
  5
Output:
  *prints tree drawing with 5 different branches*


Challenges in Development:
- Trouble with asking for amount of branches even when tree wasn't chosen
- Trouble with tree getting crunched into a ball
- Trouble with ideas
'''''