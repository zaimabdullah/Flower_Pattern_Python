import turtle

turtle.bgcolor('black')
turtle.speed(0)
colours = ['blue', 'green', 'purple', 'red', 'yellow']

for i in range(200):
    turtle.pencolor(colours[i%5])
    turtle.circle(190-i, 90)
    turtle.left(90)
    turtle.circle(190-i, 90)
    turtle.left(18)

turtle.hideturtle()