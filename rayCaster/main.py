import math
import pygame as pg

from .inputs import handle_inputs
from .entities import Barrier, Roamer
from .ray_operations import translate, get_closest_intersection


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.roamer = Roamer(250, 250)
        self.barriers = [Barrier() for _ in range(6)]

    def main_loop(self):
        while True:
            handle_inputs(self.roamer)
            self.screen.fill((0, 0, 0))
            self.draw_first_person_view()
            self.draw_minimap()
            self.clock.tick(20)
            pg.display.update()

    def draw_first_person_view(self):
        for i, ray in enumerate(self.roamer.rays):
            end_pos, distance = get_closest_intersection(ray, self.barriers)
            if not end_pos:
                continue
            distance = distance * math.cos(ray.angle)
            c = translate(distance, 0, self.roamer.view_distance, 255, 0)
            w = 15
            h = translate(distance, 0, self.roamer.view_distance, 750, 0)
            x = translate(i, 0, len(self.roamer.rays), 0, 500)
            y = translate(distance, 0, self.roamer.view_distance, 0, 250)
            pg.draw.rect(self.screen, (c, c, c), (x, y, w, h), 0)

    def draw_minimap(self):
        pg.draw.rect(self.screen, (255, 0, 0), (400, 400, 100, 100), 0)
        for i in [0, -1]:
            pg.draw.line(self.screen, (0, 0, 0), self.roamer.coordinates_for_minimap(),
                         self.roamer.rays[i].minimap_endpoint(), 1)
        for barrier in self.barriers:
            mm_start, mm_end = barrier.coordinates_for_minimap()
            pg.draw.line(self.screen, (255, 255, 255), mm_start, mm_end, 1)
