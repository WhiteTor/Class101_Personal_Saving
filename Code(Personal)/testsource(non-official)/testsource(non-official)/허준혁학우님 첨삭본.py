import pygame
import sys
from pygame.locals import QUIT

def ranking():

    rankingboard = pygame.image.load("rankingboard.png")
    screen.blit(rankingboard,(0,0))  #  ŷȭ       
    screen.blit(backImg,(10,10))

 # for text in board:
 #   text.append(board.readline())
  
 # BLACK = (0, 0, 0)
 # font = pygame.font.Font(None, 80)
 # txt = font.render(str(board), True, BLACK)


    if event.type == pygame.MOUSEBUTTONUP:
        mouse2 = pygame.mouse.get_pos()
        if 160 > mouse2[0] > 10 and 185 > mouse2[1] > 10:
            return

def quit():
    pygame.quit()
    sys.exit()

run = True

def mainmenu():
    global run
    global event
    local = [0,0]

    while run:
        screen.fill((0,0,0))
        screen.blit(background,(0,0))  #   ȭ       
        screen.blit(startImg,(200,370))  #   ۹ ư ǥ  
        screen.blit(rankingImg,(200,490))  #  ŷ  ư ǥ  
        screen.blit(settingImg,(200,610))  #   ù ư ǥ  
        screen.blit(quitImg,(200,730))   #       ư ǥ  


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                local[0] = mouse[0]
                local[1] = mouse[1]
                print(local)
            if 436 > local[0] > 200 and 470 > local[1] > 370:
                gamestart()

            elif 436 > local[0] > 200 and 590 > local[1] > 490:
                ranking()

            elif 436 > local[0] > 200 and 710 > local[1] > 610:
                setting()

            elif 436 > local[0] > 200 and 830 > local[1] > 730:
                quit()
            
                

            pygame.display.update()
            clock.tick(30)

pygame.init()
screen = pygame.display.set_mode((641, 860))
background = pygame.image.load("s.jpg")
pygame.display.set_caption("2048 game by Class101")
clock = pygame.time.Clock()

startImg = pygame.image.load("gamestart.png")
rankingImg = pygame.image.load("r.png")
settingImg = pygame.image.load("setting.png")
quitImg = pygame.image.load("quit.png")
backImg = pygame.image.load("back.png")

mainmenu()