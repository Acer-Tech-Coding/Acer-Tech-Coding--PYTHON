import turtle

window = turtle.Screen()
window.title("Square Drawing")
window.bgcolor("white")

pen = turtle.Turtle()
pen.speed(1)

for _ in range(4):
    pen.forward(100)
    pen.left(90)

pen.hideturtle()
window.mainloop()
    