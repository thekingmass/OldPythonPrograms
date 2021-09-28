'''
python turtle
* it is a toolkit which provides simple and enjoyable way to draw picture on windows or screen
* it refers to controlling a graphical entity in a graphics window with (x,y) coordinates
* Turtle graphics is a key feature of the logo programing language. It is developed for kids

'''

from turtle import *

t = Turtle()# here Turtle is a class in python and we are creating a object t for the class to use its functions
wn = Screen()# Screen is a class which can contro the attributes of graphics window

wn.title("First graphics")# title function used to change the title of the window
wn.bgcolor("cyan")# it is used to change the background color
wn.bgpic("")# it is used to set a picture as the background. it can only take a gif file

t.shape('turtle')# used to change the shape we can use circle,arrow,square, triangle and classic. By default it is classic
t.color("red", "green")# used to change the color of the color of the shape. it takes two arguments one is pen color and second is fill color
                           # here red is pen color and green is fill color

t.forward(100)# it used to move the shape forward it takes the arguments in pixel

#t.speed(1)
t.left(135)# used to move the direction of the shape
t.forward(78)

t.left(90)
t.forward(78)

t.hideturtle()# it used to hide the turtle shape

''' we are creating a square '''
t.begin_fill()
t.color('#285078', '#a0c8f0')
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.end_fill()

t.penup()# used to put the pen up

t.forward(100)
t.left(45)
t.pendown()# used to put the pen down
t.begin_fill()
t.color('#FF3399', '#00FF00')
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
done()# done() method works as getch it stop the window screen. done function should always be at the last
