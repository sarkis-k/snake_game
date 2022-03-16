from turtle import Turtle

MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0,0),(-20,0),(-40,0)]


class Snake:
    """Snake class to initiate the snake"""

    def __init__(self):
        self.snake_shape = []
        self.create_snake()
        self.head = self.snake_shape[0]

    def create_snake(self):
        """Creates initial length of 3 snake"""
        for x in POSITIONS:
            self.add_bit(x)

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

    def add_bit(self, position):
        snake_bit = Turtle()
        snake_bit.color("white")
        snake_bit.shape("square")
        snake_bit.penup()
        snake_bit.goto(position)
        self.snake_shape.append(snake_bit)

    def extend(self):
        # add new bit to snake
        self.add_bit(self.snake_shape[-1].position())