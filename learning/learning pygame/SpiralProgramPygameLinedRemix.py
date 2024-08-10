image_appending_list=[]
z=0
program_running = True
import pygame,random, time
pygame.init()
game_display=pygame.display.set_mode((600,500))
game_display.fill((200,32,32))
image = pygame.image.load("smileyFaceEmoji.png")
image = pygame.transform.scale(image, (75, 75))

while program_running:
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            game_display.blit(image, (x, y))
            image = pygame.transform.scale(image, (75, 75))
            z+=1
            image_appending_list.append(image)
            if z > 10:
                pass
        if event.type == pygame.QUIT: 
            program_running = False
            print(f"Program is closing") 
    pygame.display.update()


