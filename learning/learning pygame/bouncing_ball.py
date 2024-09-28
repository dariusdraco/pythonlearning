import pygame as pg
import time as tm
import math as mt

length = 400
breadth = 400
x_y_int = 40
speed_time_delay = 90
rate = 3

len_ball_move = mt.sqrt((length**2) + (breadth**2))
print(len_ball_move)
program_running = True
white = (255,255,255)
game_display=pg.display.set_mode((length,breadth))
game_display.fill(white)

x,y = x_y_int,x_y_int
while program_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit(0)
    tm.sleep(abs(speed_time_delay) / 1000)
    if x < len_ball_move - x_y_int:
        speed_time_delay =- rate
        game_display.fill(white)        
        pg.draw.circle(game_display,(255,0,0),(x ,y),30)
        x += 1
        y += 1
    else:
        x , y = x_y_int,x_y_int
    pg.display.update()
    