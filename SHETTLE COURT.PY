import turtle
ground=turtle.Screen()
ground.bgpic("ground.png")
ground.setup(900,900)

ground.addshape("LEFT.gif")
ground.addshape("RIGHT.gif")
ground.addshape("ball.gif")
rightplayer=turtle.Turtle()
rightplayer.penup()
rightplayer.shape("RIGHT.gif")
rightplayer.goto(400,-200)

def rightplayerup():
    y=rightplayer.ycor()
    y-=10
    if y<+250:
       y=+250
    rightplayer.sety(y)

def rightplayerdown():
    y=rightplayer.ycor()
    y-=10
    if y<-250:
        y=-250
    rightplayer.sety(y)


def rightplayerright():
    x=rightplayer.xcor()
    x-=10
    if x<+400:
        x=+400
    rightplayer.setx(x)
def rightplayerleft():
    x=rightplayer.xcor()
    x-=10
    if x<-400:
        x=-400
    rightplayer.setx(x)


turtle.onkeypress(rightplayerup,"Up")
turtle.onkeypress(rightplayerdown,"Down")
turtle.onkeypress(rightplayerright,"Right")
turtle.onkeypress(rightplayerleft,"Left")

leftplayer=turtle.Turtle()
leftplayer.penup()
leftplayer.shape("LEFT.gif")
leftplayer.goto(-400,200)

rightpen=turtle.Turtle()
rightpen.penup()
rightpen.hideturtle()
rightpen.goto(30,250)
rightpen.color("white")
rightpen.write("Rightplayer score: 0",font=("Courier",27,"bold"))


leftpen=turtle.Turtle()
leftpen.penup()
leftpen.hideturtle()
leftpen.goto(-450,250)
leftpen.color("white")
leftpen.write("Leftplayer Score: 0",font=("Courier",27,"bold"))

ball=turtle.Turtle()
ball.penup()
ball.shape("ball.gif")
ball.speed(1000)

def leftplayerup():
    y=leftplayer.ycor()
    y-=10
    if y<+250:
        y=+250
    leftplayer.sety(y)
def leftplayerdown():
    y=leftplayer.ycor()
    y-=10
    if y<-250:
        y=-250
    leftplayer.sety(y)


def leftplayerright():
    x=leftplayer.xcor()
    x-=10
    if x<+400:
        x=+400
    leftplayer.setx(x)
def leftplayerleft():
    x=leftplayer.xcor()
    x-=10
    if x<-400:
        x=-400
    leftplayer.setx(x)


turtle.onkeypress(leftplayerup,"w")
turtle.onkeypress(leftplayerdown,"s")
turtle.onkeypress(leftplayerright,"d")
turtle.onkeypress(leftplayerleft,"a")



turtle.listen()
dx=5
dy=-5
leftscore=0
rightscore=0
while True:
    x=ball.xcor()
    y=ball.ycor()
    ball.setpos(x+dx,y+dy)

    if rightplayer.distance(ball)<10:
        dx=-dx
    if leftplayer.distance(ball)<10:
        dx=-dx   
    if ball.ycor()<-280:
        dy=-dy
    if ball.ycor()>280:
        dy=-dy  
        
          
    if ball.xcor() < -450 :
        ball.goto(0,0)
        rightpen.clear()
        rightscore=rightscore+1
        rightpen.write(("Rightplayer Score: {}").format(rightscore),font=("Courier",27,"bold"))
       


    if ball.xcor() > 450 :
        ball.goto(0,0)
        leftpen.clear()
        leftscore=leftscore+1
        leftpen.write(("Leftplayer Score: {}").format(leftscore),font=("Courier",27,"bold"))
        


