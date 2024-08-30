# Python program to draw hexagon
# Using Turtle Programming
import turtle
t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("orange")
t.pencolor("white")
t.pensize(7)
t.speed(2)

num_sides = 9
side_length = 90 
angle = 360.0 / num_sides

for i in range(num_sides):
  t.forward(side_length)
  # t.backward(side_length)
  # t.left(angle)
  t.right(angle)
  
  
turtle.done()