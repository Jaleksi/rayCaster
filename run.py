import pygame as pg
from rayCaster.main import Game

WIDTH, HEIGHT = 800, 600

if __name__ == '__main__':
    pg.init()
    pg.display.set_caption('rayCaster')
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    game = Game(screen, clock)
    game.main_loop()
