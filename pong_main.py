import turtle

wn = turtle.Screen()  # wn = window
wn.title('Pong by @LucyWinters')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Pen
Player1 = 0
Player2 = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: {} AI: {}".format(Player1, Player2), align='center', font=("Courier", 24, 'normal'))

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # sets the speed to maximum possible speed in turtle
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # sets the speed to maximum possible speed in turtle
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # sets the speed to maximum possible speed in turtle
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 2  # ball moves by 2 pixles
ball.dy = 2


# Function
def paddle_a_up():
    y = paddle_a.ycor()  # ycor from turtle module returns y coordinates
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()  # ycor from turtle module returns y coordinates
    y += -20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()  # ycor from turtle module returns y coordinates
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()  # ycor from turtle module returns y coordinates
    y += -20
    paddle_b.sety(y)


# keyboard binding
wn.listen()  # turtle method to listen to keyboard typings
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')

# Main game loop
while True:
    wn.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border, Bounce ball off floor and ceiling
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # reverses the direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # reverses the direction of ball

    # Border, If ball passes Paddle, point scored and ball reset
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        Player1 = Player1 + 1
        pen.clear()
        pen.write("Player 1: {} AI: {}".format(Player1, Player2), align='center', font=("Courier", 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        Player2 = Player2 + 1
        pen.clear()
        pen.write("Player 1: {} AI: {}".format(Player1, Player2), align='center', font=("Courier", 24, 'normal'))

    # Paddle hits Ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.dx *= -1

    if ball.ycor() + 40 > paddle_b.ycor():
        paddle_b_up()
    if ball.ycor() - 40 < paddle_b.ycor():
        paddle_b_down()
