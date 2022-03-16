from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

game_is_on = True

snake = Snake()
bite = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detecting collision with food
    if snake.head.distance(bite) < 15:
        bite.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with walls
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on = False
        score.game_over()

    # detecting collision with tail
    for bits in snake.snake_shape[1:]:
        if snake.head.distance(bits) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
