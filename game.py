import pygame
pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Racing Game")
screen.fill((119,119,119))
pygame.display.update()

#close button
bumped=False
while not bumped:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            bumped = True
