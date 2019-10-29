import turtle
import os
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")
turtle.register_shape("player.gif")
turtle.register_shape("invader.gif")
#Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)

border_pen.hideturtle()

score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Draw player
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Move player left and right

def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = -280
	player.setx(x)

def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)

def fire_bullet():
	global bulletstate
	if bulletstate == "ready":
		bulletstate = "fire"		
		bullet.setposition(player.xcor(), player.ycor() + 10)
		bullet.showturtle()
		os.system("afplay laser.wav&")

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
	if distance < 15:
		return True
	else:
		return False

#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


number_of_enemies = 5
enemies = []

for i in range(number_of_enemies):
	#Create the enemy
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color("Red")
	enemy.shape("invader.gif")
	enemy.penup()
	enemy.speed(0)

	enemy.setposition(random.randint(-200, 200), random.randint(100, 250))

enemyspeed = 2

#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

bulletstate = "ready"

#Main game loop

while True:
	for enemy in enemies:
		#Move the enemy
		enemy.setx(enemy.xcor() + enemyspeed)
		#Move the enemy back and down
		if enemy.xcor() > 280:
			enemyspeed *= -1
			for e in enemies:
				e.sety(e.ycor() - 40)

		if enemy.xcor() < -280:
			enemyspeed *= -1
			for e in enemies:
				e.sety(e.ycor() - 40)

		if isCollision(bullet, enemy):
			os.system("afplay explosion.wav&")
			bullet.hideturtle()
			bulletstate = "ready"
			score += 10
			scorestring = "Score: %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
			bullet.setposition(0, -400)
			enemy.setposition(random.randint(-200, 200), 
				random.randint(100, 250))

		if isCollision(player, enemy):
			player.hideturtle()
			print("Game Over")
			break

	if bulletstate == "fire":	
		bullet.sety(bullet.ycor() + bulletspeed)

	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"



