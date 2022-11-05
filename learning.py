import turtle
ds = turtle.Turtle()
ds.speed(30)

for i in range (230):
    ds.forward(10)
    ds.right(225)
    ds.forward(102)
    ds.left(30)
    ds.forward(70)
    ds.right(30)

    ds.penup()
    ds.setposition(2, 0 )
    ds.pendown()
    ds.right(2)
turtle.done()