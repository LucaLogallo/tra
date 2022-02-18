import turtle  # basic graphic
import os
from tkinter import *
import sys

wn = turtle.Screen()  # mi creo una finestra
wn.title("pong by luca logallo")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
scoreA = 0
scoreB = 0

# paddle a
paddleA = turtle.Turtle()
paddleA.speed(0)  # speed animation
paddleA.shape("square")  # rettangolo
paddleA.color("white")  # colore
paddleA.shapesize(stretch_wid=6, stretch_len=0.5)
paddleA.penup()
paddleA.goto(-350, 0)

# paddle b
paddleB = turtle.Turtle()
paddleB.speed(0)  # speed animation
paddleB.shape("square")  # rettangolo
paddleB.color("white")  # colore
paddleB.shapesize(stretch_wid=6, stretch_len=0.5)
paddleB.penup()
paddleB.goto(+350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# ball x move
ball.dx = 2  # 2 pixel in x
# ball y move
ball.dy = 2  # 2 pixel in y
# functions


# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player A: 0  player B: 0", align="center",
          font=("Courier", 24, "normal"))


def paddleA_up():
    y = paddleA.ycor()
    y += 30
    paddleA.sety(y)


def paddleA_down():
    y = paddleA.ycor()
    y -= 30
    paddleA.sety(y)


def paddleB_up():
    y = paddleB.ycor()
    y += 30
    paddleB.sety(y)


def paddleB_down():
    y = paddleB.ycor()
    y -= 30
    paddleB.sety(y)


# binding keyboards
wn.listen()
wn.onkeypress(paddleA_up, "w")
wn.onkeypress(paddleA_down, "s")
wn.onkeypress(paddleB_up, "Up")
wn.onkeypress(paddleB_down, "Down")
# main game loop
while True:
    wn.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border hit
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("player A: {} player B: {}".format(scoreA, scoreB),
                  align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("player A: {} player B: {}".format(scoreA, scoreB), align="center",
                  font=("Courier", 24, "normal"))
    # paddle and ball collision
    if ball.xcor() < -340 and ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50:
        ball.goto(0, 0)
        ball.dx *= -1
        #os.system("afplay bounce.wav&")
        # playsound('D:/t/tra/games/bounce.mp3')
    if ball.xcor() > 340 and ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50:
        ball.goto(0, 0)
        ball.dx *= -1
        #os.system("afplay bounce.wav&")
        # playsound('D:/t/tra/games/bounce.mp3')
