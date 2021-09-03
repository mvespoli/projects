import turtle

#question
available_colours = ["green", "red", "blue", "white"]
number_of_players = input ("Choose the number of players: ")
if number_of_players == "4":
    a = input ("Choose between " + str(available_colours) + " Player 1: ")
    available_colours.remove(a)
    b = input ("Choose between " + str(available_colours) + " Player 2: ")
    available_colours.remove(b)
    c = input ("Choose between " + str(available_colours) + " Player 3: ")
    available_colours.remove(c)
    d = input ("Choose between " + str(available_colours) + " Player 4: ")
    available_colours.remove(d)

elif number_of_players == "3":
    a = input ("Choose between " + str(available_colours) + " Player 1: ")
    available_colours.remove(a)
    b = input ("Choose between " + str(available_colours) + " Player 2: ")
    available_colours.remove(b)
    c = input ("Choose between " + str(available_colours) + " Player 3: ")
    available_colours.remove(c)
elif number_of_players == "2":
    a = input ("Choose between " + str(available_colours) + " Player 1: ")
    available_colours.remove(a)
    b = input ("Choose between " + str(available_colours) + " Player 2: ")
    available_colours.remove(b)

else: 
    print("Choose at least 2 players: ")

#score
lives_a = 3
lives_b = 3
lives_c = 3
lives_d = 3

if "green" in available_colours:
    lives_a = 0

if "blue" in available_colours:
    lives_b = 0

if "red" in available_colours:
    lives_c = 0

if "white" in available_colours:
    lives_d = 0


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)


#Visual
visual_a = turtle.Turtle()
visual_a.shape("square")
visual_a.color("pink")
visual_a.penup()
visual_a.shapesize(stretch_wid=.01,stretch_len=38.975)
visual_a.goto(0,290)

visual_b = turtle.Turtle()
visual_b.shape("square")
visual_b.color("pink")
visual_b.penup()
visual_b.shapesize(stretch_wid=.01,stretch_len=38.975)
visual_b.goto(0,-290)

visual_c = turtle.Turtle()
visual_c.shape("square")
visual_c.color("pink")
visual_c.penup()
visual_c.shapesize(stretch_wid=28.975,stretch_len=.01)
visual_c.goto(390,0)

visual_d = turtle.Turtle()
visual_d.shape("square")
visual_d.color("pink")
visual_d.penup()
visual_d.shapesize(stretch_wid=28.975,stretch_len=.01)
visual_d.goto(-390,0)

#PaddlebA
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Paddle C
paddle_c = turtle.Turtle()
paddle_c.speed(0)
paddle_c.shape("square")
paddle_c.color("red")
paddle_c.shapesize(stretch_wid=1,stretch_len=5)
paddle_c.penup()
paddle_c.goto(0,250)

#Paddle D
paddle_d = turtle.Turtle()
paddle_d.speed(0)
paddle_d.shape("square")
paddle_d.color("white")
paddle_d.shapesize(stretch_wid=1,stretch_len=5)
paddle_d.penup()
paddle_d.goto(0,-250)

global pause
pause = True
#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx = .2
ball.dy = .2

#pen
pen_c = turtle.Turtle()
pen_c.speed(0)
pen_c.color("white")
pen_c.penup()
pen_c.hideturtle()
pen_c.goto(0,258)
pen_c.write("3", align="center", font=("Courier", 24, "normal"))

pen_d = turtle.Turtle()
pen_d.speed(0)
pen_d.color("white")
pen_d.penup()
pen_d.hideturtle()
pen_d.goto(0,-295)
pen_d.write("3", align="center", font=("Courier", 24, "normal"))

pen_a = turtle.Turtle()
pen_a.speed(0)
pen_a.color("white")
pen_a.penup()
pen_a.hideturtle()
pen_a.goto(-378,0)
pen_a.write("3", align="center", font=("Courier", 24, "normal"))

pen_b = turtle.Turtle()
pen_b.speed(0)
pen_b.color("white")
pen_b.penup()
pen_b.hideturtle()
pen_b.goto(378,0)
pen_b.write("3", align="center", font=("Courier", 24, "normal"))

#winner text
winner_a = turtle.Turtle()
winner_a.speed(0)
winner_a.color("green")
winner_a.hideturtle()
winner_a.goto(0,0)

winner_b = turtle.Turtle()
winner_b.speed(0)
winner_b.color("blue")
winner_b.hideturtle()
winner_b.goto(0,0)

winner_c = turtle.Turtle()
winner_c.speed(0)
winner_c.color("red")
winner_c.hideturtle()
winner_c.goto(0,0)

winner_d = turtle.Turtle()
winner_d.speed(0)
winner_d.color("white")
winner_d.hideturtle()
winner_d.goto(0,0)



#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if y <= 240:
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if y >= -240:
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if y <= 240:
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    if y >= -240:
        paddle_b.sety(y)

def paddle_c_right():
    x = paddle_c.xcor()
    x += 20
    if x <= 340:
        paddle_c.setx(x)

def paddle_c_left():
    x = paddle_c.xcor()
    x -= 20
    if x >= -340:
        paddle_c.setx(x)

def paddle_d_right():
    x = paddle_d.xcor()
    x += 20
    if x <= 340:
        paddle_d.setx(x)

def paddle_d_left():
    x = paddle_d.xcor()
    x -= 20
    if x >= -340:
        paddle_d.setx(x)

def game_start():
    global pause 
    pause = not pause 
    
#Key Binds
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
wn.onkeypress(paddle_c_right,"y")
wn.onkeypress(paddle_c_left,"t")
wn.onkeypress(paddle_d_right,".")
wn.onkeypress(paddle_d_left,",")
wn.onkeypress(game_start,"space")
acceleration = 0 
speed_modifier = 1

#game loop

while True:
    wn.update()
    if pause:
        continue
        
    acceleration += 1

    if acceleration == 1000:
        acceleration = 0
        speed_modifier += 0.1
    #move ball
    ball.setx(ball.xcor()+ball.dx*speed_modifier)
    ball.sety(ball.ycor()+ball.dy*speed_modifier)

    if lives_a <= 0:
        paddle_a.color("black")
        paddle_a.goto(-9999999,-9999999)
        if ball.xcor() < -380:
            ball.setx(-380)
            ball.dx *=-1 
    else:
        if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *=-1
            lives_a -= 1
            speed_modifier = 1
            pen_a.clear()
            pen_a.write("{}".format(lives_a), align="center", font=("Courier", 24, "normal"))
    
    if lives_b <= 0:
        paddle_b.color("black")
        paddle_b.goto(-9999999,-9999999)
        if ball.xcor() > 380:
            ball.setx(380)
            ball.dx *=-1 
    else:
        if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx *=-1 
            lives_b -= 1
            speed_modifier = 1
            pen_b.clear()
            pen_b.write("{}".format(lives_b), align="center", font=("Courier", 24, "normal"))

    if lives_c <= 0:
        paddle_c.color("black")
        paddle_c.goto(-9999999,-9999999)
        if ball.ycor() > 280:
            ball.sety(280)
            ball.dy *=-1 
    else:
        if ball.ycor() > 290:
            ball.goto(0,0)
            ball.dy *=-1
            lives_c -= 1
            speed_modifier = 1
            pen_c.clear()
            pen_c.write("{}".format(lives_c), align="center", font=("Courier", 24, "normal"))
        
    if lives_d <= 0:
        paddle_d.color("black")
        paddle_d.goto(-9999999,-9999999)
        if ball.ycor() < -280:
            ball.sety(-280)
            ball.dy *=-1 
    else:
        if ball.ycor() < -290:
            ball.goto(0,0)
            ball.dy *=-1
            lives_d -= 1
            speed_modifier = 1
            pen_d.clear()
            pen_d.write("{}".format(lives_d), align="center", font=("Courier", 24, "normal"))

    # bounce
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *=-1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *=-1

    if (ball.ycor() > 240 and ball.ycor() < 250) and (ball.xcor() < paddle_c.xcor() + 50 and ball.xcor() > paddle_c.xcor() -50):
        ball.sety(240)
        ball.dy *=-1
    if (ball.ycor() < -240 and ball.xcor() > -250) and (ball.xcor() < paddle_d.xcor() + 50 and ball.xcor() > paddle_d.xcor() -50):
        ball.sety(-240)
        ball.dy *=-1

    if lives_a != 0 and lives_b == 0 and lives_c == 0 and lives_d == 0:
        winner_a.write("Player Green Wins!", align="center", font=("Courier", 34, "normal"))

    if lives_b != 0 and lives_a == 0 and lives_c == 0 and lives_d == 0:
        winner_b.write("Player Blue Wins!", align="center", font=("Courier", 34, "normal"))
    
    if lives_c != 0 and lives_b == 0 and lives_a == 0 and lives_d == 0:
        winner_c.write("Player Red Wins!", align="center", font=("Courier", 34, "normal"))
    
    if lives_d != 0 and lives_b == 0 and lives_c == 0 and lives_a == 0:
        winner_d.write("Player White Wins!", align="center", font=("Courier", 34, "normal"))

