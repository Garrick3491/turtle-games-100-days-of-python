from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()

colors = ["red", "orange", "aqua", "green", "blue", "purple"]

screen.setup(width=500, height=400)
y_pos = -100
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter red, orange, aqua, green, blue or purple: ")

all_turtles = []

for _ in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[_])
    turtle.goto(x=-230, y=y_pos)
    all_turtles.append(turtle)
    y_pos += 25

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You Win! The winning color is {winning_turtle}")
            else:
                print(f"You Lose! The winning color is {winning_turtle}")





screen.exitonclick()
