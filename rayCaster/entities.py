import math
from random import randint

from .ray_operations import translate, intersects, points_distance, intersect_point


class Barrier:
    def __init__(self):
        self.start_pos = (randint(0, 500), randint(0, 500))
        self.end_pos = (randint(0, 500), randint(0, 500))

    def coordinates_for_minimap(self, width, height):
        start_x = int(translate(self.start_pos[0], 0, width, width - 100, width))
        start_y = int(translate(self.start_pos[1], 0, height, height - 100, height))
        end_x = int(translate(self.end_pos[0], 0, width, width - 100, width))
        end_y = int(translate(self.end_pos[1], 0, height, height - 100, height))
        return (start_x, start_y), (end_x, end_y)


class Roamer:
    def __init__(self, width, height):
        self.x = width // 2
        self.y = height // 2
        self.w = width
        self.h = height
        self.dir_angle = math.radians(0)
        self.view_distance = 100
        self.fov = 90
        self.rays = self.create_rays()

    def create_rays(self):
        rays = []
        angle_difference = self.fov / self.w
        angle = self.w / 2 * angle_difference * -1
        for i in range(self.w):
            rays.append(Ray(self, angle, i))
            angle += angle_difference
        return rays
    
    def turn(self, direction):
        self.dir_angle += math.radians(direction)

    def move(self, speed):
        self.x = self.x + int(speed * math.cos(self.dir_angle))
        self.y = self.y + int(speed * math.sin(self.dir_angle))

    def coordinates_for_minimap(self):
        mapped_x = int(translate(self.x, 0, self.w, self.w - 100, self.w))
        mapped_y = int(translate(self.y, 0, self.h, self.h - 100, self.h))
        return (mapped_x, mapped_y)


class Ray:
    def __init__(self, parent, angle, index):
        self.parent = parent
        self.angle = math.radians(angle)
        self.index = index
        self.endpoint = None

    def calculate_endpoint(self):
        end_x = self.parent.x + int(self.parent.view_distance * math.cos(
            self.parent.dir_angle + self.angle))
        end_y = self.parent.y + int(self.parent.view_distance * math.sin(
            self.parent.dir_angle + self.angle))
        self.endpoint = (end_x, end_y)

    def minimap_endpoint(self, width, height):
        mapped_x = int(translate(self.endpoint[0], 0, width, width - 100, width))
        mapped_y = int(translate(self.endpoint[1], 0, height, height - 100, height))
        return (mapped_x, mapped_y)

    def get_closest_intersection(self, barriers):
        self.calculate_endpoint()
        distance_to_closest_intersection = math.inf
        closest_intersection = None
        ray_start = (self.parent.x, self.parent.y)
        for barrier in barriers:
            if not intersects(ray_start, self.endpoint, barrier.start_pos, barrier.end_pos):
                continue
            found_intersect = intersect_point(ray_start, self.endpoint,
                                              barrier.start_pos, barrier.end_pos)
            distance = points_distance(ray_start, found_intersect)
            if distance > distance_to_closest_intersection:
                continue
            distance_to_closest_intersection = distance
            closest_intersection = found_intersect
        return closest_intersection, distance_to_closest_intersection

    def get_rect(self, distance, w, h):
        distance *= math.cos(self.angle)
        vd = self.parent.view_distance

        color = translate(distance, 0, vd, 255, 0)
        width = 1
        height = translate(distance, 0, vd, h * 1.5, 0)
        x = self.index
        y = translate(distance, 0, vd, 0, h / 2)
        return (x, y, width, height), (color, color, color)
