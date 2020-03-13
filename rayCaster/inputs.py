import sys

import pygame as pg

def handle_inputs(roamer):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                roamer.move(5)
            elif event.key == pg.K_DOWN:
                roamer.move(-5)
            elif event.key == pg.K_LEFT:
                roamer.turn(-10)
            elif event.key == pg.K_RIGHT:
                roamer.turn(10)
