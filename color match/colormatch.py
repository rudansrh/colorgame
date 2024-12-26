import pygame
import sys
import time
pygame.init()

#화면 크기 설정
screen_width = 800
screen_height = 550
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Color Match")

red_cir = pygame.image.load("이미지 저장\\red.png")
red_cir = pygame.transform.scale(red_cir,(30,30))
green_cir = pygame.image.load("이미지 저장\\green.png")
green_cir = pygame.transform.scale(green_cir,(30,30))
blue_cir = pygame.image.load("이미지 저장\\blue.png")
blue_cir = pygame.transform.scale(blue_cir,(30,30))
triangle = pygame.image.load("이미지 저장\\TRIANGLE.png")
triangle = pygame.transform.scale(triangle,(80,80))
myFont = pygame.font.Font("CookieRun Regular.ttf", 30)

#색 설정
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
bgcolor = (0,0,0)

enemysize = (1000,30)
circlepos = [(400-15,250-15),(425-15,290-15),(375-15,290-15),(0,0)]
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(bgcolor)
    screen.blit(triangle, (360,230))
    screen.blit(red_cir,circlepos[0])
    screen.blit(blue_cir,circlepos[1])
    screen.blit(green_cir,circlepos[2])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                circlepos[3] = circlepos[0]
                circlepos[0] = circlepos[1]
                circlepos[1] = circlepos[2]
                circlepos[2] = circlepos[3]
            if event.key == pygame.K_LEFT:
                circlepos[3] = circlepos[2]
                circlepos[2] = circlepos[1]
                circlepos[1] = circlepos[0]
                circlepos[0] = circlepos[3]
    
    pygame.display.flip()