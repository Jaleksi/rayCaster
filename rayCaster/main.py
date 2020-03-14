from random import randint
import math

import pygame as pg

from .inputs import handle_inputs
from .entities import Barrier, Roamer
from .ray_operations import intersects, intersect_point, points_distance, translate


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.roamer = Roamer(self, 250, 250)
        self.barriers = self.new_barriers(6)

    def main_loop(self):
        while True:
            handle_inputs(self.roamer)
            self.screen.fill((0, 0, 0))
            self.draw()
            self.clock.tick(20)
            pg.display.update()

    def new_barriers(self, number_of_barriers):
        barriers = []
        for _ in range(number_of_barriers):
            start_pos = (randint(10, 490), randint(10, 490))
            end_pos = (randint(10, 490), randint(10, 490))
            barriers.append(Barrier(self, start_pos, end_pos))
        return barriers

    def draw(self):
        for i, angle in enumerate(self.roamer.ray_angles):
            end_pos, distance = self.get_ray_endpoint(angle)
            if not end_pos:
                continue
            distance = distance * math.cos(angle)
            c = translate(distance, 0, self.roamer.view_distance, 255, 0)
            #w = translate(distance, 0, self.roamer.view_distance, 15, 1)
            w = 15
            h = translate(distance, 0, self.roamer.view_distance, 500, 0)
            x = translate(i, 0, len(self.roamer.ray_angles), 0, 500)
            y = translate(distance, 0, self.roamer.view_distance, 0, 250)
            pg.draw.rect(self.screen, (c, c, c), (x, y, w, h), 0)

    def get_ray_endpoint(self, angle):
        ray_start_point = (self.roamer.x, self.roamer.y)
        ray_end_point = (self.roamer.x + int(self.roamer.view_distance
                                             * math.cos(self.roamer.dir_angle + angle)),
                         self.roamer.y + int(self.roamer.view_distance
                                             * math.sin(self.roamer.dir_angle + angle)))
        distance_to_closest_intersect = 999999999
        intersecting_point = None
        for barrier in self.barriers:
            if not intersects(ray_start_point, ray_end_point,
                              barrier.start_pos, barrier.end_pos):
                continue
            found_intersect =  intersect_point(ray_start_point, ray_end_point,
                                               barrier.start_pos, barrier.end_pos)
            distance = points_distance(ray_start_point, found_intersect)
            if distance > distance_to_closest_intersect:
                continue
            distance_to_closest_intersect = distance
            intersecting_point = found_intersect
        return intersecting_point, distance_to_closest_intersect
