#Jerico Branch
#3/20/2025
#P4Lab1
#Learning turtle graphics and loops

import turtle
#Create drawing window
win = turtle.Screen()
#Create turtle object
timmy = turtle.Turtle()

# Set some attributes
timmy.pensize(8)
timmy.pencolor('purple')
timmy.shape('arrow')
win.bgcolor('blue')

#Test
#timmy.forward(100)

#For loop to draw triangle
for i in range (3):
    timmy.forward(200)
    timmy.left(120)

#While loop to draw a square
side_num = 0

while side_num <= 3: 
    timmy.forward(200)
    timmy.right(90) 
    side_num += 1





#Keeps the window open
win.mainloop()