from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("green")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def grow(self):
        # Add new segment at the last segment's position
        last_pos = self.segments[-1].position()
        self.add_segment(last_pos)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):
        # Move all existing segments off-screen
        for segment in self.segments:
            segment.goto(1000, 1000)  # Hide off-screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
