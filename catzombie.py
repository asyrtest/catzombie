import pygame
from pygame import mixer
mixer.init()

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #song
    pygame.mixer.music.load("IntroSong.mp3")
    pygame.mixer.music.play(-1)
    
    #game logo and name      
    pygame.display.set_caption("CatZombie The Game")
    icon=pygame.image.load("cat-mask.png")
    pygame.display.set_icon(icon)

    #wallpaper
    image=pygame.image.load("grass.jpg").convert()
    screen.blit(image, (500, 500))
    
    pygame.display.flip()
