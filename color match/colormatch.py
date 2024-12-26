import pygame
import sys
import time
pygame.init()

#화면 크기 설정정
screen_width = 800
screen_height = 550
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Color Match")

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
circlepos = [(400,250),(425,290),(375,290),(0,0)]
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(bgcolor)
    screen.blit(triangle, (360,230))
    circle1 = pygame.draw.circle(screen, red, circlepos[0], 10)
    circle2 = pygame.draw.circle(screen, green, circlepos[1], 10)
    circle3 = pygame.draw.circle(screen, yellow, circlepos[2], 10)
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