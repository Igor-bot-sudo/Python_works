import turtle


positions = ((0.0, 136.60), (50.0, 50.0), (-50.0, 50.0))

def draw_hexagon():
    for i in range(6):
        turtle.forward(100)
        turtle.right(60)
        

turtle.width(2)
turtle.pencolor('blue')
turtle.speed(4)
turtle.right(180)
for i in positions:
    turtle.penup()
    turtle.goto(i)
    turtle.pendown()
    turtle.right(120)
    draw_hexagon()

turtle.exitonclick()
