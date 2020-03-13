import math


class Barrier:
    def __init__(self, game, start_pos, end_pos):
        self.game = game
        self.start_pos = start_pos
        self.end_pos = end_pos


class Roamer:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.dir_angle = math.radians(0)

    def turn(self, direction):
        self.dir_angle += math.radians(direction)

    def move(self, distance):
        self.x = self.x + int(distance * math.cos(self.dir_angle))
        self.y = self.y + int(distance * math.sin(self.dir_angle))
