import turtle
turtle.Screen().bgcolor("light blue")
turtle.Screen().setup(300,400)

polygon = turtle.Turtle()

num_sides = 4
side_length = 70
angle = 360.0 / num_sides


polygon.forward(side_length)
polygon.right(angle)

polygon.forward(side_length)
polygon.right(angle)

polygon.forward(side_length)
polygon.right(angle)

polygon.forward(side_length)
polygon.right(angle)
    
turtle.done( )