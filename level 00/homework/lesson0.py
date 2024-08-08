from turtle import *

#we want to paint a house

# step 1 draw a square
speed(10)
color("purple")
width(7)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square
#drawing a door
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)


penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#drawing a window
penup()
color("red")
begin_fill()
goto(140,140)
pendown()

left(120)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)
right(90)
end_fill()

penup()
forward(80)
pendown()

color("red")
begin_fill()
forward(40)
right(90)

forward(40)
right(90)

forward(40)
right(90)

forward(40)
right(90)
end_fill()
exitonclick()