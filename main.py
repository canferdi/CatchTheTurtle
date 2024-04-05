import turtle
import random
import time

# Screen
screen = turtle.Screen()
screen.title("Catch the Turtle")
screen.setup(800, 800)
screen.bgcolor("Light Blue3")

# Score
scoreTurtle = turtle.Turtle(visible=False)
scoreTurtle.color("blue")
scoreTurtle.penup()
topHeight = screen.window_height() / 2
y = topHeight * 0.9
scoreTurtle.setpos(0, y)

# Tortoise
tortoise = turtle.Turtle(visible=False)
tortoise.color("green")
tortoise.shape("turtle")
tortoise.shapesize(3)

# Countdown
countdownTurtle = turtle.Turtle(visible=False)
countdownTurtle.color("dark red")
countdownTurtle.penup()
topHeight = screen.window_height() / 2
y = topHeight * 0.8
countdownTurtle.setpos(0, y)

FONT = ("Arial", 30, "normal")
score = 0
gameOver = False


def move():
    if not gameOver:
        turtle.tracer(0)
        tortoise.penup()
        x = random.randint(-350, 350)
        y = random.randint(-350, 350)
        tortoise.setx(x)
        tortoise.sety(y)
        tortoise.showturtle()
        turtle.tracer(1)
        screen.ontimer(move, 600)  # Tortoise move speed


def writeScore():
    scoreTurtle.write(arg="Score: 0", move=False, align="center", font=FONT)


def countdown(time):
    countdownTurtle.clear()
    if time > 0:
        countdownTurtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        global gameOver
        gameOver = True
        tortoise.hideturtle()
        countdownTurtle.write(arg="GAME OVER!!!", move=False, align="center", font=FONT)


def handleClic(x, y):
    global score
    score += 1
    scoreTurtle.clear()
    scoreTurtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)


def startGame():
    writeScore()
    countdown(10)   # GameOver time
    move()
    tortoise.onclick(handleClic)


startGame()
turtle.mainloop()
