from turtle import *
t = Turtle()
wn = Screen()
wn.setup(700,600)
wn.title('Stamp pattern')
t.color('darkgoldenrod', 'black')
#t.setpos(25, 0)

gd = 10
for i in range(50):
    gd = gd + 2
    t.stamp()
    t.forward(gd)
    t.right(25)
done()

