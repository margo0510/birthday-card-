import pygame 
import time 

pygame.init()

WIDTH = 600
HEIGHT = 600 

display_surface = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Birthday Greeting")
img = pygame.image.load("bg.jpeg")
image = pygame.transform.scale(img, (600,600))

while True:
    font = pygame.font.SysFont("Times New Roman", 70)
    text_1 = font.render("Happy", True, (50,20,100))
    text_2 = font.render("Birthday", True, (50,20,100))
    display_surface.fill("white")
    display_surface.blit(image, (0,0))
    display_surface.blit(text_1, (210,180))
    display_surface.blit(text_2, (180,260))
    pygame.display.update()
    time.sleep(2)

    image_2 = pygame.image.load("present.jpeg")
    font_2 = pygame.font.SysFont("Arial", 36)
    text_3 = font_2.render("wish you a happy future", True, (200,100,130))
    display_surface.fill("white")
    display_surface.blit(image_2, (0,0))
    display_surface.blit(text_3, (30,30))
    pygame.display.update()
    time.sleep(2)

    

    



time.sleep(10)