
import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Снайпер")
icon = pygame.image.load("img/yP9EzmDF1dY.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/205798053943a1cdfa9d6fda7446a83c.jpg")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


runnig = True
while runnig:
    pass




pygame.quit()