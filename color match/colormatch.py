import pygame
import sys
import time
import random
pygame.init()

score = 0
e_size = 50
start = 0
end = 0

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

again = pygame.image.load("이미지 저장\\again.png")
again = pygame.transform.scale(again,(80,80))
againRect = pygame.Rect(370, 330, 80,80)

myFont = pygame.font.Font("CookieRun Regular.ttf", 40)
tjfaudFont = pygame.font.Font("CookieRun Regular.ttf", 30)

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
lasta = 0
lastc = 0
playerstate = 0 #0: 왼-빨, 오른-파  1: 왼-파, 오른-빨

running = True
while running:
    clock.tick(60)
    screen.fill(bgcolor)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mousepos = event.pos
            if end == 1 and againRect.collidepoint(mousepos):
                #재시작
                cooltime = 1.3
                startTime = pygame.time.get_ticks()
                enemylist = []
                lasta = 0
                lastc = 0
                playerstate = 0 
                score = 0
                start = 0
                end = 0
                continue
            elif start == 0: 
                start = 1
                startTime = pygame.time.get_ticks()
            elif start == 1:
                playerstate = 1-playerstate
                
    if end == 1:
        myFont = pygame.font.Font("CookieRun Regular.ttf", 60)
        scoreText = myFont.render(f"점수 : {score}", True,white)
        screen.blit(scoreText, (300, 200))
        screen.blit(again, (370,330))
        pygame.display.flip()
        continue
    
    if playerstate == 0:
        screen.blit(player1, (335, 200))
    else:
        screen.blit(player2, (335, 200))
    
    if score < 10:
        textpos = (370, 10)
    elif score < 100:
        textpos = (355, 10)
    else:
        textpos = (345, 10)
    scoreText = myFont.render(f"{score}점", True,white)
    screen.blit(scoreText, textpos)
    
    if start == 1:
        tjfaudText = tjfaudFont.render("마우스 클릭으로 플레이", True,white)
        screen.blit(tjfaudText, (275, 490))
    else:
        tjfaudText = tjfaudFont.render("- Click To Start -", True,white)
        screen.blit(tjfaudText, (285, 490))
    
    if start == 0:
        pygame.display.flip()
        continue
        
    dell = -1
    for i in range(len(enemylist)):
        enemylist[i][0][0] += enemylist[i][1]*speed
        e_rect = pygame.Rect(int(enemylist[i][0][0]),int(enemylist[i][0][1]),e_size,e_size)
        if len(enemylist[i]) == 4:
            imageE = enemylist[i][3]
            imageE.set_alpha(imageE.get_alpha()-10)
            if imageE.get_alpha() <= 0:
                dell = i
            screen.blit(imageE, tuple(enemylist[i][0]))
        else:
            if e_rect.colliderect(Lrect) or e_rect.colliderect(Rrect):
                if playerstate == 0:
                    if (enemylist[i][1] == 1 and enemylist[i][2] == 0) or (enemylist[i][1] == -1 and enemylist[i][2] == 1):
                        score += 10
                    else:
                        time.sleep(1)
                        end = 1
                else:
                    if (enemylist[i][1] == 1 and enemylist[i][2] == 1) or (enemylist[i][1] == -1 and enemylist[i][2] == 0):
                        score += 10
                    else:
                        time.sleep(1)
                        end = 1
                if enemylist[i][2] == 0:
                    test = pygame.image.load("이미지 저장\\red.png")
                    test = pygame.transform.scale(test,(e_size,e_size))
                else:
                    test = pygame.image.load("이미지 저장\\blue.png")
                    test = pygame.transform.scale(test,(e_size,e_size))
                test.set_alpha(180)
                enemylist[i].append(test)
            screen.blit(circles[enemylist[i][2]], tuple(enemylist[i][0]))
    if dell != -1:
        del(enemylist[dell])    
        
    if (pygame.time.get_ticks() - startTime)/1000 > cooltime:
        startTime = pygame.time.get_ticks()
        if cooltime > mincooltime:
            cooltime -= 0.015
            cooltime = round(cooltime,3)
        while 1:
            a = random.randint(1,2)
            c = random.randint(0,1)
            if a != lasta or c != lastc:
                lastc = c
                lasta = a
                break
        if a == 1:
            s_pos = [-90,225]
            direc = 1
            enemylist.append([s_pos, direc, c])
        else:
            s_pos = [820, 225]
            direc = -1
            enemylist.append([s_pos, direc, c])
            
    pygame.display.flip()