import turtle


turtle.penup()
turtle.goto((-50, 50))
turtle.width(5)
turtle.pencolor('brown')
turtle.pendown()

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.left(30)
for i in range(4):
    turtle.left(30)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)

turtle.exitonclick()
