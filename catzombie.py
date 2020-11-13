import pygame
from pygame import mixer
mixer.init()

pygame.init()
screen = pygame.display.set_mode((1000, 500))
done = False
#song
pygame.mixer.music.load("IntroSong.mp3")
pygame.mixer.music.play(-1)

#game logo and name      
pygame.display.set_caption("CatZombie The Game")
icon=pygame.image.load("cat-mask.png")
pygame.display.set_icon(icon)

#wallpaper
image=pygame.image.load("grass.jpg").convert()
screen.blit(image, (0, 0))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
