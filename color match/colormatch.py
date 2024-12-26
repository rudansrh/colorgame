import pygame
import sys
import time
import random
pygame.init()

score = 0
e_size = 50

#화면 크기 설정
screen_width = 800
screen_height = 550
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Color Match")

player1 = pygame.image.load("이미지 저장\\player1.png")
player1 = pygame.transform.scale(player1,(130,100))
player2 = pygame.image.load("이미지 저장\\player2.png")
player2 = pygame.transform.scale(player2,(130,100))

r_cir = pygame.image.load("이미지 저장\\red.png")
r_cir = pygame.transform.scale(r_cir,(e_size,e_size))
b_cir = pygame.image.load("이미지 저장\\blue.png")
b_cir = pygame.transform.scale(b_cir,(e_size,e_size))
circles = [r_cir, b_cir]

myFont = pygame.font.Font("CookieRun Regular.ttf", 40)

#색 설정
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
bgcolor = (0,0,0)

Lrect = pygame.Rect(345,230,50,50)
Rrect = pygame.Rect(405,230,50,50)

enemylist = [] #[pos, dir(+1,-1), color]

speed = 4
cooltime = 1.3
mincooltime = 0.5
clock = pygame.time.Clock()
startTime = 0
playerstate = 0 #0: 왼-빨, 오른-파  1: 왼-파, 오른-빨

running = True
while running:
    clock.tick(60)
    screen.fill(bgcolor)
    if playerstate == 0:
        screen.blit(player1, (335, 200))
    else:
        screen.blit(player2, (335, 200))
    scoreText = myFont.render(f"{score}", True,white)
    screen.blit(scoreText, (390, 10))
    
    dell = -1
    for i in range(len(enemylist)):
        enemylist[i][0][0] += enemylist[i][1]*speed
        e_rect = pygame.Rect(int(enemylist[i][0][0]),int(enemylist[i][0][1]),e_size,e_size)
        screen.blit(circles[enemylist[i][2]], tuple(enemylist[i][0]))
        if e_rect.colliderect(Lrect) or e_rect.colliderect(Rrect):
            if playerstate == 0:
                if (enemylist[i][1] == 1 and enemylist[i][2] == 0) or (enemylist[i][1] == -1 and enemylist[i][2] == 1):
                    score += 10
                else:
                    running = False
            else:
                if (enemylist[i][1] == 1 and enemylist[i][2] == 1) or (enemylist[i][1] == -1 and enemylist[i][2] == 0):
                    score += 10
                else:
                    running = False
            dell = i
    if dell != -1:
        del(enemylist[dell])
        
    if (pygame.time.get_ticks() - startTime)/1000 > cooltime:
        startTime = pygame.time.get_ticks()
        if cooltime > mincooltime:
            cooltime -= 0.01
        a = random.randint(1,2)
        if a == 1:
            s_pos = [-90,220]
            direc = 1
            c = random.randint(0,1) #0:빨, 1:파
            enemylist.append([s_pos, direc, c])
        else:
            s_pos = [820, 220]
            direc = -1
            c = random.randint(0,1) #0:빨, 1:파
            e_image = circles[c]
            enemylist.append([s_pos, direc, c])
            
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            playerstate = 1-playerstate
    pygame.display.flip()