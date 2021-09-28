from turtle import *
from time import sleep

t = Turtle()  # here Turtle is a class in python and we are creating a object t for the class to use its functions
wn = Screen()  # Screen is a class which can control the attributes of graphics window
wn.setup(900, 700)
wn.title("Ludo By Turtle Graphics")
t.speed(15)

t.penup()
t.goto(-400, 270)
t.pendown()

# making the outline
t.pensize(4)
for i in range(4):
    t.fd(600)
    t.rt(90)
t.lt(90)


# making the background lines
def lines():
    t.pensize(1)
    for i in range(7):
        t.rt(90)
        t.fd(40)
        t.rt(90)
        t.fd(600)
        t.lt(90)
        t.fd(40)
        t.lt(90)
        t.fd(600)


lines()  # making horizontal lines

t.rt(90)
t.fd(40)

lines()  # making vertical lines
t.rt(90)
t.fd(40)

def square():
    t.pensize(4)
    t.begin_fill()
    for i in range(4):
        t.right(90)
        t.fd(240)
    t.end_fill()
    t.rt(90)
    t.fd(40)
    t.up()
    t.rt(90)
    t.fd(40)
    t.lt(180)
    t.down()
    t.begin_fill()
    t.color('pink', 'pink')
    for i in range(4):
        t.right(90)
        t.fd(160)
    t.end_fill()
    t.pensize(1)

    ''' 
       making the tokens space in the small square
       '''
    t.rt(90)
    t.fd(60)
    t.rt(90)
    t.fd(40)
    ''' above code is for moving the turtle from small square border to inside the square to make the token circle'''

    t.rt(180)
    t.begin_fill()
    t.color('white', 'white')
    t.circle(20)
    t.end_fill()

    t.up()
    t.rt(90)
    t.fd(80)
    t.lt(90)
    t.down()
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    t.up()
    t.bk(80)
    t.down()
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    t.up()
    t.lt(90)
    t.fd(80)
    t.rt(90)
    t.down()
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    t.up()
    t.lt(90)
    t.fd(60)
    t.rt(90)
    t.fd(120)



    t.shape('turtle')
    t.color('black', 'black')
def positioning():
    t.penup()
    t.fd(40)
    t.rt(90)
    t.fd(560)
    t.down()

# making the blue square
# t.begin_fill()
t.color('Blue', 'Blue')
square()
positioning()

# making the red square
t.color('red', 'red')
square()
positioning()

# making the green square
t.color('green', 'green')
square()
positioning()

# making the yellow square
t.color('#FFFF00', '#FFFF00')
square()

# All squares have been made now making the home ways

t.bk(200)
t.rt(180)
t.down()


# making the home ways
def homeway():
    t.fd(80)
    t.lt(90)
    t.fd(200)
    t.rt(90)
    t.fd(40)
    t.lt(135)
    t.fd(84)
    t.lt(90)
    t.fd(84)
    t.lt(135)
    t.fd(40)
    t.rt(90)
    t.fd(160)
    t.rt(90)
    t.fd(40)

def homeposition():
    t.up()
    t.bk(320)
    t.rt(90)
    t.fd(160)
    t.down()

#  making the home way for yellow square
t.pensize(3)
t.color('#FFFF00', '#FFFF00')
homeway()

#  making home way for green color

t.color('green', 'green')
homeposition()
homeway()

#  making the home way for red square
t.color('red', 'red')
homeposition()
homeway()

#  making the home way for blue square
t.color('blue', 'blue')
homeposition()
homeway()


done()