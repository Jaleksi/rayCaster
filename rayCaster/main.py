import pygame as pg

from .inputs import handle_inputs
from .entities import Barrier, Roamer


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = pg.display.get_surface().get_size()
        self.roamer = Roamer(self.width, self.height)
        self.barriers = [Barrier() for _ in range(6)]

    def main_loop(self):
        while True:
            handle_inputs(self.roamer)
            self.screen.fill((0, 0, 0))
            self.draw_first_person_view()
            self.draw_minimap()
            self.draw_fps()
            self.clock.tick(20)
            pg.display.update()

    def draw_fps(self):
        fps_text = 'FPS: ' + '{0:.2f}'.format(self.clock.get_fps())
        fps = pg.font.Font(None, 30).render(fps_text, True, (255, 255, 255))
        self.screen.blit(fps, (0, 0))

    def draw_first_person_view(self):
        for i, ray in enumerate(self.roamer.rays):
            end_pos, distance = ray.get_closest_intersection(self.barriers)
            if not end_pos:
                continue
            rect_dimensions, color = ray.get_rect(distance, self.width, self.height)
            pg.draw.rect(self.screen, color, rect_dimensions)

    def draw_minimap(self):
        pg.draw.rect(self.screen, (255, 0, 0), (self.width - 100, self.height - 100,
                                                100, 100), 0)
        for i in [0, -1]:
            pg.draw.line(self.screen, (0, 0, 0),
                         self.roamer.coordinates_for_minimap(),
                         self.roamer.rays[i].minimap_endpoint(self.width, self.height),
                         1)
        for barrier in self.barriers:
            mm_start, mm_end = barrier.coordinates_for_minimap(self.width, self.height)
            pg.draw.line(self.screen, (255, 255, 255), mm_start, mm_end, 1)
