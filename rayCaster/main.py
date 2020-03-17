import math
import pygame as pg

from .inputs import handle_inputs
from .entities import Barrier, Roamer
from .ray_operations import translate, calculate_endpoint, get_closest_intersection


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
            self.draw()
            self.clock.tick(20)
            pg.display.update()

    def draw(self):
        # Draw firstperson-view
        for i, angle in enumerate(self.roamer.ray_angles):
            end_pos, distance = get_closest_intersection(self.roamer.x, self.roamer.y,
                                                         angle, self.barriers,
                                                         self.roamer.view_distance,
                                                         self.roamer.dir_angle)
            if not end_pos:
                continue
            distance = distance * math.cos(angle)
            c = translate(distance, 0, self.roamer.view_distance, 255, 0)
            w = 15
            h = translate(distance, 0, self.roamer.view_distance, 750, 0)
            x = translate(i, 0, len(self.roamer.ray_angles), 0, 500)
            y = translate(distance, 0, self.roamer.view_distance, 0, 250)
            pg.draw.rect(self.screen, (c, c, c), (x, y, w, h), 0)
        # Draw minimap
        pg.draw.rect(self.screen, (255, 0, 0), (400, 400, 100, 100), 0)
        for i in [0, -1]:
            angle = self.roamer.ray_angles[i]
            ray_end = calculate_endpoint(self.roamer.x, self.roamer.y,
                                         angle, self.roamer.view_distance,
                                         self.roamer.dir_angle)
            roamer_mapped_x = int(translate(self.roamer.x, 0, 500, 400, 500))
            roamer_mapped_y = int(translate(self.roamer.y, 0, 500, 400, 500))
            ray_end_mapped_x = int(translate(ray_end[0], 0, 500, 400, 500))
            ray_end_mapped_y = int(translate(ray_end[1], 0, 500, 400, 500))
            pg.draw.line(self.screen, (0, 0, 0), (roamer_mapped_x, roamer_mapped_y),
                         (ray_end_mapped_x, ray_end_mapped_y), 1)

        for b in self.barriers:
            mm_start_x = int(translate(b.start_pos[0], 0, 500, 400, 500))
            mm_start_y = int(translate(b.start_pos[1], 0, 500, 400, 500))
            mm_end_x = int(translate(b.end_pos[0], 0, 500, 400, 500))
            mm_end_y = int(translate(b.end_pos[1], 0, 500, 400, 500))
            pg.draw.line(self.screen, (255, 255, 255),
                         (mm_start_x, mm_start_y), (mm_end_x, mm_end_y), 1)
