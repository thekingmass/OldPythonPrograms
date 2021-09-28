from turtle import *
from time import sleep

t = Turtle()  # here Turtle is a class in python and we are creating a object t for the class to use its functions
wn = Screen()  # Screen is a class which can control the attributes of graphics window
wn.setup(900, 700)
wn.title("Ludo By Turtle Graphics")
t.speed(20)
t.penup()
t.goto(-400, 270)
t.pendown()
# sleep(5)
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


lines()

t.rt(90)
t.fd(40)

lines()
t.rt(90)
t.fd(40)


# making the squares for tokens


def square():
    t.pensize(4)
    for i in range(4):
        t.right(90)
        t.fd(240)
    t.rt(90)
    t.fd(40)
    t.up()
    t.rt(90)
    t.fd(40)
    t.lt(180)
    t.down()
    t.begin_fill()
    for i in range(4):
        t.right(90)
        t.fd(160)
    t.end_fill()
    t.pensize(1)
    ''' 
    making the tokens space in the small square
    '''
    t.rt(90)
    t.fd(30)
    t.rt(90)
    t.fd(40)
    def pos():
        t.lt(90)
        t.fd(60)
    def circle():
        t.color('white', 'white')
        t.begin_fill()
        t.circle(20)
        t.end_fill()
    pos()
    circle()

    pos()
    circle()


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
# t.end_fill()

'''
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
positioning()
'''

#all squares have been made now making the home ways

'''
t.up()
t.rt(180)
t.fd(240)
t.lt(90)
t.fd(40)
t.rt(90)
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


#  making home way for blue color
t.pensize(3)
t.color('Blue', 'Blue')
homeway()

def homeposition():
    t.up()
    t.bk(320)
    t.rt(90)
    t.fd(160)
    t.down()


#  making the home way for yellow square
t.color('#FFFF00', '#FFFF00')
homeposition()
homeway()

#  making the home way for green square
t.color('green', 'green')
homeposition()
homeway()

#  making the home way for red square
t.color('red', 'red')
homeposition()
homeway()
'''

done()
