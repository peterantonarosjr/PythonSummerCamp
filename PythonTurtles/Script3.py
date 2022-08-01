#Import the library
import turtle

#Separate window
screen = turtle.getscreen()

#Create a turtle object
t = turtle.Turtle()

#Set the window title
turtle.title("Super cool TURTLE program!")

#Set the turtle color
t.color('red','yellow')

#Fill in the shapes made
t.begin_fill()

#Set the screen bg color
turtle.bgcolor("grey")

#Basic turtle commands
while True:
     t.forward(200)
     t.left(170)

     #Stopping condition so this doesn't run forever
     if abs(t.pos()) < 1:
          break

#End the filling of shapes made
t.end_fill()

#Keep the window open until we close it
turtle.mainloop()
