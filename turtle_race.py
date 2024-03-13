from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Male your bet", prompt="Which turtle will win the race "
                                                          "(red,orange,yellow,green,blue,purple)? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    timy = Turtle()
    timy.color(colors[turtle_index])
    timy.shape("turtle")
    timy.penup()
    timy.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(timy)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print("You win !!")
            else:print(f"you lose , the winnnig turtle is {winning_turtle} ")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()