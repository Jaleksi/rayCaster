from random import randint
import math

import pygame as pg

from .inputs import handle_inputs
from .entities import Barrier, Roamer


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.roamer = Roamer(self, 250, 250)
        self.barriers = self.new_barriers(1)

    def main_loop(self):
        while True:
            handle_inputs(self.roamer)
            self.screen.fill((255, 255, 255))
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
        for barrier in self.barriers:
            pg.draw.line(self.screen, (0, 0, 0), barrier.start_pos, barrier.end_pos, 1)
        pg.draw.circle(self.screen, (0, 0, 0), (self.roamer.x, self.roamer.y), 3)

        start_pos = (self.roamer.x, self.roamer.y)

        end_pos = (self.roamer.x + int(150 * math.cos(self.roamer.dir_angle)),
                   self.roamer.y + int(150 * math.sin(self.roamer.dir_angle)))
        pg.draw.line(self.screen, (0, 0, 0), start_pos, end_pos, 1)

