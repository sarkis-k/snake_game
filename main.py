from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake_shape = []
game_is_on = True

for x in range(0, 3):
    snake_bit = Turtle()
    snake_bit.color("white")
    snake_bit.shape("square")
    snake_bit.penup()
    snake_bit.goto(-20*x, 0)
    snake_shape.append(snake_bit)


while game_is_on:
    screen.update()
    time.sleep(1)
    for seg in range(len(snake_shape)-1, 0, -1):
        new_x = snake_shape[seg-1].xcor()
        new_y = snake_shape[seg-1].ycor()
        snake_shape[seg].goto(new_x, new_y)
    snake_shape[0].forward(20)
    snake_shape[0].left(90)


screen.exitonclick()