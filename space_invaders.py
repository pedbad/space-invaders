#Space Invaders
#python 2.7.12 on Mac

import turtle
import os

#Set up the screen

win = turtle.Screen()
win.bgcolor("black")
win.title("Space Invaders")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pensize(3)
border_pen.pendown()
for side in range(4):
  border_pen.fd(600)
  border_pen.lt(90)
border_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.speed(0)
player.penup()
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Create the enemy turtle
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.speed(0)
enemy.penup()
enemy.setposition(-200, 250)

enemyspeed = 2




#Move the player left and right

def move_left():
  x = player.xcor()
  x = x - playerspeed
  if x < -280:
    x = -280
  player.setx(x)

def move_right():
  x = player.xcor()
  x = x + playerspeed
  if x > 280:
    x = 280
  player.setx(x)


#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")


#Main game loop
while True:
  #This is a forever loop
  #Move the enemy
  x = enemy.xcor()
  x = x + enemyspeed
  enemy.setx(x)

  #Move enemy back and down
  if enemy.xcor() > 280:
    enemyspeed =  enemyspeed * -1
    y = enemy.ycor()
    y = y - 40
    enemy.sety(y)
  if enemy.xcor() < -280:
    enemyspeed = enemyspeed  * -1
    y = enemy.ycor()
    y = y - 40
    enemy.sety(y)



delay = raw_input("Press enter to finish")