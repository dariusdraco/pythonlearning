import pygame as pg
display = pg.display.set_mode((500,500))
display.fill((0,0,0))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit(0)
    pg.time.Clock(60)
    pg.display.update()
    pg.draw.circle(display,(204,34,0),(250,250),100)
    