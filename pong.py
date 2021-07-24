@@ -0,0 +1,119 @@
import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("Black")
window.setup(width=800, height=600)
window.tracer(0)

#Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.color("Green")
paddle_1.penup()
paddle_1.goto(-350,0)

#Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.color("Green")
paddle_2.penup()
paddle_2.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("Green")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2


#Score_Screen
score = turtle.Turtle()
score.speed(0)
score.color("Green")
score.penup()
score.hideturtle()
score.goto(0, 270)
score.write("Player 1: 0     Player 2: 0", align="center", font= ("Courier", 24, "normal"))

Score_1 = 0
Score_2 = 0

#Functions
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)



#Keyboard Bindings
window.listen()
window.onkey(paddle_1_up, "w")
window.onkey(paddle_1_down, "s")

window.onkey(paddle_2_up, "i")
window.onkey(paddle_2_down, "k")

#Main Loop
open = True
while open:
    window.update()

    #Move Ball
    ball.setx((ball.xcor() + ball.dx))
    ball.sety(ball.ycor() + ball.dy)

    #Boundary Conditions
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        Score_1 += 1
        score.clear()
        score.write("Player 1: {}     Player 2: {}".format(Score_1, Score_2), align="center", font= ("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        Score_2 += 1
        score.clear()
        score.write("Player 1: {}     Player 2: {}".format(Score_1, Score_2), align="center", font= ("Courier", 24, "normal"))
    #BallPaddleBounce
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor()+50 and ball.ycor() > paddle_2.ycor()-50): 
        ball.setx(340)
        ball.dx*=-1     

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor()+50 and ball.ycor() > paddle_1.ycor()-50): 
        ball.setx(-340)
        ball.dx*=-1 