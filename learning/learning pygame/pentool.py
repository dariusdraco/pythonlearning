import pygame as pg, random as rndm
red = (255,0,0)
program_running = True
game_display = pg.display.set_mode((600,500))
game_display.fill((255,255,255))
x, y = 0,0
pendown = False
while program_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            program_running = False
            quit(0)
        if event.type == pg.MOUSEBUTTONDOWN:
            old_x, old_y = x, y = event.pos
            pendown = True
        if event.type == pg.MOUSEBUTTONUP:    
            old_x, old_y = x, y
            pendown = False
        if event.type == pg.MOUSEMOTION and pendown:
            x, y = event.pos
            pg.draw.line(game_display,red,(old_x,old_y),(x,y),5)
            old_x, old_y = x, y

    pg.display.update()