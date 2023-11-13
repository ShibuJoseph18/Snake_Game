from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x_coordinate = self.segments[segment_num - 1].xcor()
            new_y_coordinate = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x_coordinate, new_y_coordinate)
        self.head.forward(MOVING_DISTANCE)
        print(self.head.position())

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
