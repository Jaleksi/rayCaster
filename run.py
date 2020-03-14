import pygame as pg
from rayCaster.main import Game


if __name__ == '__main__':
    pg.init()
    pg.display.set_caption('rayCaster')
    screen = pg.display.set_mode((500, 500))
    clock = pg.time.Clock()
    game = Game(screen, clock)
    game.main_loop()
