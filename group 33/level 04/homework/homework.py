import turtle


screen = turtle.Screen()
screen.bgcolor("white")


pen = turtle.Turtle()
pen.speed(5)


pen.penup()
pen.goto(-250, -250)  
pen.pendown()
pen.begin_fill()
pen.color("gray")
for _ in range(2):
    pen.forward(400)
    pen.left(90)
    pen.forward(250)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(-300, -150)
pen.pendown()
pen.begin_fill()
pen.color("black")
for _ in range(2):
    pen.forward(100)
    pen.left(90)
    pen.forward(200)
    pen.left(90)
pen.end_fill()


pen.penup()
pen.goto(150, -150)
pen.pendown()
pen.begin_fill()
pen.color("black")
for _ in range(2):
    pen.forward(100)
    pen.left(90)
    pen.forward(200)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(-240, 0)  
pen.pendown()
pen.begin_fill()
pen.color("brown")
pen.goto(0, 200)  
pen.goto(200, 0)  
pen.goto(-200, 0)  
pen.end_fill()

pen.penup()
pen.goto(-30, -150)
pen.pendown()
pen.begin_fill()
pen.color("green")
for _ in range(2):
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
pen.end_fill()