from random import randint
import math

import pygame as pg

from .inputs import handle_inputs
from .entities import Barrier, Roamer
from .ray_operations import intersects, intersect_point


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.roamer = Roamer(self, 250, 250)
        self.barriers = self.new_barriers(3)

    def main_loop(self):
        while True:
            handle_inputs(self.roamer)
            self.screen.fill((255, 255, 255))
            self.draw()
            self.clock.tick(30)
            pg.display.update()

    def new_barriers(self, number_of_barriers):
        barriers = []
        for _ in range(number_of_barriers):
            start_pos = (randint(10, 490), randint(10, 490))
            end_pos = (randint(10, 490), randint(10, 490))
            barriers.append(Barrier(self, start_pos, end_pos))
        return barriers

    def draw(self):
        for barrier in self.barriers:
            pg.draw.line(self.screen, (0, 0, 0), barrier.start_pos, barrier.end_pos, 1)
        pg.draw.circle(self.screen, (0, 0, 0), (self.roamer.x, self.roamer.y), 3)

        start_pos = (self.roamer.x, self.roamer.y)

        fov_ray_angles = [math.radians(i*2) for i in range(-20, 20)]

        for angle in fov_ray_angles:
            pg.draw.line(self.screen, (0, 0, 0), start_pos,
                         self.get_ray_endpoint(angle), 1)

    def get_ray_endpoint(self, angle):
        ray_start_point = (self.roamer.x, self.roamer.y)
        ray_end_point = (self.roamer.x + int(self.roamer.view_distance
                                             * math.cos(self.roamer.dir_angle + angle)),
                         self.roamer.y + int(self.roamer.view_distance
                                             * math.sin(self.roamer.dir_angle + angle)))
        for barrier in self.barriers:
            if not intersects(ray_start_point, ray_end_point,
                              barrier.start_pos, barrier.end_pos):
                continue
            return intersect_point(ray_start_point, ray_end_point,
                                   barrier.start_pos, barrier.end_pos)
        return ray_end_point
