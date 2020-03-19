import math
from random import randint

from .ray_operations import translate


class Barrier:
    def __init__(self):
        self.start_pos = (randint(0, 500), randint(0, 500))
        self.end_pos = (randint(0, 500), randint(0, 500))

    def coordinates_for_minimap(self):
        start_x = int(translate(self.start_pos[0], 0, 500, 400, 500))
        start_y = int(translate(self.start_pos[1], 0, 500, 400, 500))
        end_x = int(translate(self.end_pos[0], 0, 500, 400, 500))
        end_y = int(translate(self.end_pos[1], 0, 500, 400, 500))
        return (start_x, start_y), (end_x, end_y)


class Roamer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir_angle = math.radians(0)
        self.view_distance = 100
        self.fov = 50
        self.rays = [Ray(self, i) for i in range(-self.fov//2, self.fov//2)]

    def turn(self, direction):
        self.dir_angle += math.radians(direction)

    def move(self, speed):
        self.x = self.x + int(speed * math.cos(self.dir_angle))
        self.y = self.y + int(speed * math.sin(self.dir_angle))

    def coordinates_for_minimap(self):
        mapped_x = int(translate(self.x, 0, 500, 400, 500))
        mapped_y = int(translate(self.y, 0, 500, 400, 500))
        return (mapped_x, mapped_y)


class Ray:
    def __init__(self, parent, angle):
        self.parent = parent
        self.angle = math.radians(angle)

    def endpoint(self):
        end_x = self.parent.x + int(self.parent.view_distance * math.cos(
            self.parent.dir_angle + self.angle))
        end_y = self.parent.y + int(self.parent.view_distance * math.sin(
            self.parent.dir_angle + self.angle))
        return (end_x, end_y)

    def minimap_endpoint(self):
        end_p = self.endpoint()
        mapped_x = int(translate(end_p[0], 0, 500, 400, 500))
        mapped_y = int(translate(end_p[1], 0, 500, 400, 500))
        return (mapped_x, mapped_y)
