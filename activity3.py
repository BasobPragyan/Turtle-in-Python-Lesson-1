import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(500,600)
t= turtle.Turtle()
t.shape("turtle")
t_pen = turtle.Turtle()
size=0
while True:
    for i in range(4):
        t_pen.forward(size+1)
        t_pen.left(90)
        size = size - 5
        size = size + 1
turtle.done()