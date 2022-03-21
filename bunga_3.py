import turtle

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
turtle.bgcolor('black')
turtle.speed(0)

def bulatan(saiz):
  for i in range(1,11):
    for j in range(1,11):
      turtle.circle(150 - j*saiz)
    turtle.right(360/10)

warna = ['blue', 'green', 'violet', 'orange', 'cyan']

for x in range(5):
  turtle.pencolor(warna[x%5])
  bulatan(x+1)

turtle.done()