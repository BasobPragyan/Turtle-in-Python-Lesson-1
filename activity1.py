import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(500,600)
t= turtle.Turtle()
t.shape("turtle")
sides=int(input("Enter number of sides"))
angle=360/sides
len=int(input("Enter length :"))
for i in range(sides):
    t.forward(len)
    t.right(angle)

turtle.done()