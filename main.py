import turtle
import winsound
import pygame

wn = turtle.Screen()
wn.title("Pong by HOZ")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
pygame.mixer.init()

#score
score_a = 0
score_b = 0

#PAddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)   #animation speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#PAddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)   #animation speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)   #animation speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 0.05
ball.dy = 0.05     # ball moves by 2 pixels

# PEn 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0       Player B: 0", align="center", font=("Times New Roman", 22, "normal"))

# Function
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)


#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
#wn.onkeypress(paddle_a_up, "W")
wn.onkeypress(paddle_a_down, "s")
#wn.onkeypress(paddle_a_down, "S")

wn.onkeypress(paddle_b_up, "Up")
#wn.onkeypress(paddle_b_up, "up")
wn.onkeypress(paddle_b_down, "Down")
#wn.onkeypress(paddle_b_down, "down")

#MAin game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290) 
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290) 
        ball.dy *= -1

    if ball.xcor() > 380:
        ball.goto(0, 0) 
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {}       Player B: {}".format(score_a, score_b), align="center", font=("Times New Roman", 22, "normal"))
        pygame.mixer.music.load("punch-2-37333.mp3")
        pygame.mixer.music.play()
        
    
    if ball.xcor() < -380:
        ball.goto(0, 0) 
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {}       Player B: {}".format(score_a, score_b), align="center", font=("Times New Roman", 22, "normal"))
        pygame.mixer.music.load("fist-punch-or-kick-7171.mp3")
        pygame.mixer.music.play()

    #paddle and ball colision
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
        pygame.mixer.music.load("punch-140236.mp3")
        pygame.mixer.music.play()

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
        pygame.mixer.music.load("punch-140236.mp3")
        pygame.mixer.music.play()