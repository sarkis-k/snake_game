from turtle import Turtle

MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Snake class to initiate the snake"""

    def __init__(self):
        self.snake_shape = []
        self.create_snake()
        self.head = self.snake_shape[0]

    def create_snake(self):
        """Creates initial length of 3 snake"""
        for x in range(0, 3):
            snake_bit = Turtle()
            snake_bit.color("white")
            snake_bit.shape("square")
            snake_bit.penup()
            snake_bit.goto(-20 * x, 0)
            self.snake_shape.append(snake_bit)

    def move(self):
        """Move all bits of the snake by the amount """
        for seg in range(len(self.snake_shape) - 1, 0, -1):
            new_x = self.snake_shape[seg - 1].xcor()
            new_y = self.snake_shape[seg - 1].ycor()
            self.snake_shape[seg].goto(new_x, new_y)
        self.snake_shape[0].forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
