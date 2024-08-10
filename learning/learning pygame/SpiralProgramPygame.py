program_running = True
import pygame,random, time
pygame.init()
game_display=pygame.display.set_mode((600,500))
game_display.fill((200,32,32))
image = pygame.image.load("smileyFaceEmoji.png")
image = pygame.transform.scale(image, (75, 75))
last_10_cordinates = list()
displacement = 50
while program_running:
    time.sleep(.090)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos            
            game_display.blit(image, (x, y))
            image = pygame.transform.scale(image, (75, 75))
            last_10_cordinates.append((x,y))
            mod_last_10 = len(last_10_cordinates) % 5
            if len(last_10_cordinates) > 4 and mod_last_10 == 0:
                old_x, old_y = last_10_cordinates[0]
                if(x > old_x + displacement) or (x < old_x - displacement)\
                    or (y > old_y + displacement) or (y < old_y - displacement): 
                    (x,y) = last_10_cordinates.pop(0)
                    pygame.draw.rect(game_display, (200,32,32), (x, y, 75, 75))


        if event.type == pygame.QUIT: 
            program_running = False
            print(f"Program is closing") 
    pygame.display.update()


