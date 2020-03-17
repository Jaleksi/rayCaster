import math
from random import randint


class Barrier:
    def __init__(self):
        self.start_pos = (randint(0, 500), randint(0, 500))
        self.end_pos = (randint(0, 500), randint(0, 500))


class Roamer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir_angle = math.radians(0)
        self.view_distance = 100
        self.fov = 50
        self.ray_angles = [math.radians(i) for i in range(-self.fov//2, self.fov//2)]

    def turn(self, direction):
        self.dir_angle += math.radians(direction)

    def move(self, speed):
        self.x = self.x + int(speed * math.cos(self.dir_angle))
        self.y = self.y + int(speed * math.sin(self.dir_angle))
