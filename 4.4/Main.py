'''''
pumpkin
import turtle

wn = turtle.Screen()
wn.bgcolor("lightblue")

t = turtle.Turtle()
t.speed(8)
t.hideturtle()

def drawcircle(x,y):
  t.color("orangered")
  t.penup()
  t.goto(x,y)
  t.begin_fill()
  t.circle(70)
  t.end_fill()
drawcircle(20,0)
drawcircle(-20,0)

def triangle(x,y):
  t.color("black")
  t.penup()
  t.goto(x,y)
  t.begin_fill()
  for i in range(3):
  	t.forward(40)
	  t.left(360/3)
  t.end_fill()
triangle(15,80)
triangle(-55,80)
triangle(-20,50)

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
mouth()

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
stem()
'''''
'''''
tree
import turtle
wn = turtle.Screen()
wn.bgcolor("lightblue")

t = turtle.Turtle()
t.pencolor("white")
t.speed(67)
t.hideturtle()
true = None
def snowflake(size):
  for i in range(6)
    t.forward(size)
    if (size>6):
      snowflake(size/3)
    t.backward(size)
    t.right(60)

snowflake(150)
t.mainloop()
'''''
'''''
import turtle
wn = turtle.Screen()
wn.bgcolor("lightblue")
turtle = turtle.Turtle()

def drawTree(level, branchLength):
  if level > 0:
    turtle.forward(branchLength)
    turtle.left(40)
    drawTree(level-1, branchLength/1.67)
    
    turtle.right(80)
    drawTree(level-1, branchLength/1.67)
    
    turtle.left(40)
    turtle.back(branchLength)
  else:
    turtle.color("light green")
    turtle.stamp()
    turtle.color("brown")
turtle.speed(0)
turtle.penup()
turtle.goto(0, -180)
turtle.left(90)
turtle.pendown()

turtle.color("brown")
turtle.width(3)
turtle.shape("triangle")
levels = input("Amount of branches(max 7): ")
if levels > 7:
  levels = 7
drawTree(int(levels), 120)
'''''