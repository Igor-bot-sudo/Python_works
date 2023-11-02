import turtle

def draw_square():
    turtle.penup()
    turtle.goto((-250, 250))
    turtle.width(5)
    turtle.speed(6)
    turtle.pendown()

    for k in range(2):
        f = True
        for i in range(5):
            if f:
                turtle.forward(500)
                turtle.right(90)
                turtle.forward(100)
                turtle.right(90)
            else:
                turtle.forward(500)
                turtle.left(90)
                turtle.forward(100)
                turtle.left(90)
            f = not f
        turtle.forward(500)
        turtle.right(90)

    turtle.exitonclick()


draw_square()
