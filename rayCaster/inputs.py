import sys

import pygame as pg


def handle_inputs(roamer):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pressed = pg.key.get_pressed()
    if pressed[pg.K_UP]:
        roamer.move(5)
    elif pressed[pg.K_DOWN]:
        roamer.move(-5)
    if pressed[pg.K_LEFT]:
        roamer.turn(-5)
    elif pressed[pg.K_RIGHT]:
        roamer.turn(5)
