import turtle


screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(3)

#draw square
pen.penup()
pen.goto(-100, -100)  
pen.pendown()
pen.begin_fill()
pen.color("red")
for _ in range(4):
    pen.forward(200) 
    pen.left(90) 
pen.end_fill()


# Draw the roof
pen.penup()
pen.goto(-100, 100)  
pen.pendown()
pen.begin_fill()
pen.color("green")
pen.goto(0, 200)  
pen.goto(100, 100)  
pen.goto(-100, 100)  
pen.end_fill()

turtle.done()