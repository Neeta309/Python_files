#                         BASIC SETUP AND INITLIZATION
# Importing turtle library -- 2 ways of importing
# from turtle import * 
# or
import turtle


# Creating a Turtle Object
t = turtle.Turtle()  

# Window and Screen Configuration
s = turtle.Screen() 

# Some Screen Methods

#sets the title of the window
s.title("My Turtle Graphics")

# sets the background color of the window.
s.bgcolor("orange")

# Defines width and height of the window.
s.setup(900,500)

# Changing color function
def change_color(x, y):
    """Changes the turtle's color to a random color."""
    import random
    colors = ["red", "blue", "green", "yellow", "purple", "pink"]
    t.color(random.choice(colors))
    
#Handling Events and User Interaction
s.onclick(change_color)

turtle.mainloop()  