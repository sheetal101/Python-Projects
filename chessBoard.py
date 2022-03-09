# PROJECT 3

# Creating chessboard using turtle library 

import turtle

# create screen object
t=turtle.Turtle()

# DRAWING SQUARE

def box(n):
  for i in range(4):
    t.forward(n)
    t.left(90)
t.speed(0)

x=0
y=0
count=2

# RUNNING LOOP FOR BOARD & BOARD COLOR

while not False:
  t.goto(x,y)
  t.pendown()
  x+=20
  t.begin_fill()
  if count%2==0:
    t.fillcolor("#065f46")
  else:
    t.fillcolor("#6ee7b7")
  count+=1
  box(20)
  t.end_fill()
  if x>=20*8:
    x=0
    y+=20
    t.penup()
    count+=1
  if y>=20*8:
    break

t.hideturtle()

turtle.done()

