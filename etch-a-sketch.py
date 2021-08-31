from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()

def move_forward():
    turtle.fd(50)


def turn_left():
    turtle.lt(10)


def turn_right():
    turtle.rt(10)


def move_backwards():
    turtle.bk(50)


def reset():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=reset, key="c")

screen.listen()
screen.exitonclick()