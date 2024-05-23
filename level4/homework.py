from turtle import *
                                          
speed(5) 
color("black")     #დავიწყე მართკუთხედის ხაზვა
width(7)
color = "black"
begin_fill()
forward(300)
right(90)
forward(150)
right(90)
forward(300)
right(90)
forward(150)
right(90)         #მოვრჩი მართკუთხედის ხაზვას
end_fill() 
          

    
penup()           #დავიწყე სახურავის ხაზვა
goto(0,0)
pendown()              
left(40) 
forward(150)
right(80)
forward(150)
left(130)
forward(160)
right(90)
forward(70)
right(90)
forward(160)     #მოვრჩი სახურავის ხაზვას
end_fill()

penup()          
width(2)        
fillcolor("green") 
begin_fill()

goto(300,130)
pendown()
left(180)
forward(100)
left(90)
forward(70)
left(90)

forward(30)
left(90)
forward(70)
end_fill()
penup()
goto(100,150)
pendown()
width(5)     #დავიწყე მეორე სახურავის ხატვა
right(90)
forward(70)
right(55)
forward(50)
right(125)
forward(100)
right(90)
forward(40)

fillcolor("green")    #დავიწყე მეორე დროშის ხატვა
begin_fill()
width(2)       
left(90)
forward(80)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)   #მოვრჩი მეორე დროშის ხატვას
end_fill()

penup()       #დავიწყე მეფის ხატვა
goto(-45,-70)
pendown()
circle(20)

right(90)
forward(40)
left(30)
forward(45)

penup()
goto(-45,-70)
pendown()
right(30)
forward(40)
right(30)
forward(45)

penup()
goto(-45,-70)
pendown()
forward(50)

penup()
goto(-45,-70)
pendown()
left(70)
forward(50)

penup()       #დავიწყე დედოფლის ხატვა
goto(-120,-120)
pendown()
circle(20)

right(40)
forward(40)
left(30)
forward(45)

penup()
goto(-120,-120)
pendown()
right(30)
forward(40)
right(30)
forward(45)

penup()
goto(-120,-120)
pendown()
forward(50)

penup()
goto(-120,-120)
pendown()
left(70)
forward(50)

