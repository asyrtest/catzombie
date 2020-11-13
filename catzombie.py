#1 - Import the library
import pygame
#2 - Initialize the game
pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False
#2.1 – Add wallpaper
#2.2 – Add music
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
