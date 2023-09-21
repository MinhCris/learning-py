from turtle import Turtle , Screen

timmy_the_turtle = Turtle()

print(timmy_the_turtle)
timmy_the_turtle.color("blue")
timmy_the_turtle.shape("turtle")






for i in range(15):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.penup()
    timmy_the_turtle.right(135)
    timmy_the_turtle.pendown()








screen = Screen()
screen.exitonclick()