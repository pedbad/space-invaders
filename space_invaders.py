#Space Invaders
#python 2.7.12 on Mac

import turtle
import os
import math
import random

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

#Choose number of enemies
number_of_enemies = 5

#Create an empty list of enemies
enemiesList = []

#Add enemies to the list
#We need to create more turtle objects

for i in range(number_of_enemies):
  #Create the enemy
  enemiesList.append(turtle.Turtle())

for enemy in enemiesList:
  enemy.color("red")
  enemy.shape("circle")
  enemy.speed(0)
  enemy.penup()
  x = random.randint(-200, 200)
  y = random.randint(100, 200)
  enemy.setposition(x, y)

enemyspeed = 2

#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.speed(0)
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#Define bullet state
#we have 2 states:
#ready - ready to fire bullet
#fire - bullet is firing

bulletstate = "ready"





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

def fire_bullet():
  #Declare bulletstate as a global if it needs change
  global bulletstate
  if bulletstate == "ready": 
    #Move the bullet to just above the player
    x = player.xcor()
    y = player.ycor() + 10
    bullet.setposition(x,y)
    bullet.showturtle()
    bulletstate = "fire"


def isCollision(t1,t2):
  distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(),2))
  if distance < 15:
    return True
  else:
    return False



#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


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
    y = y - 45
    enemy.sety(y)
  if enemy.xcor() < -280:
    enemyspeed = enemyspeed  * -1
    y = enemy.ycor()
    y = y - 45
    enemy.sety(y)

  #Move the bullet only when bulletstate is "fire"
  if bulletstate == "fire":
    y = bullet.ycor()
    y = y + bulletspeed
    bullet.sety(y)

  #Check to see if bullet has reached the top
  if bullet.ycor() > 275:
    bullet.hideturtle()
    bulletstate = "ready"

  #Check for collision between bullet and enemy
  if isCollision(bullet, enemy):
    #Reset the bullet
    bullet.hideturtle()
    bulletstate = "ready"
    bullet.setposition(0, -400)
    #Reset the enemy
    enemy.setposition(-200, 250)

  #Check for collision between enemy and player
  if isCollision(player, enemy):
    player.hideturtle()
    enemy.hideturtle()
    print("GAME OVER")
    break




#delay = raw_input("Press enter to finish")