import turtle

# getting a screen to work on
ws=turtle.Screen()

# defining turtle instance
t=turtle.Turtle()

# setting up turtle color to green
t.color("Green")

#setting up width to 2
t.width("2")

# setting up speed to2
t.speed("20")

#loop for making outside square of length 300
for i in range(4):
    t.forward(300)
    t.left(90)

#code for innr lines of the square
t.penup()
t.goto(0, 100)
t.pendown()
t.forward(300)
t.penup()
t.goto(0,200)
t.pendown()
t.forward(300)
t.penup()
t.goto(100,0)
t.pendown()
t.left(90)
t.forward(300)
t.penup()
t.goto(200,0)
t.pendown()
t.forward(300)
