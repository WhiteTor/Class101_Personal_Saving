import pygame
import sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((641, 860))
background = pygame.image.load("Main.jpg")
pygame.display.set_caption("2048 game by Class101")
clock = pygame.time.Clock()

startImg = pygame.image.load("gamestart.png")
rankingImg = pygame.image.load("ranking.png")
settingImg = pygame.image.load("setting.png")
quitImg = pygame.image.load("quit.png")
backImg = pygame.image.load("back.png")

BLACK = (0, 0, 0)

def ranking():
  print("ranking")

  rankingboard = pygame.image.load("rankingboard.png")
  screen.blit(rankingboard,(0,0))  #��ŷȭ�� ����
  screen.blit(backImg,(10,10))
  board = open("ranking.txt", "r")
    
  rankinglist = []

  while True:
      line = board.readline()

      if not line:
          break

      line = line.split()
      rankinglist.append(line)
      
  board.close()
  
  y = 300
  for i in range(5):
      myFont = pygame.font.SysFont( "arial", 30, True, False)
      name = myFont.render(rankinglist[i][0], True, BLACK)
      score = myFont.render(rankinglist[i][1], True, BLACK)

      screen.blit(name, [250, y])
      screen.blit(score, [410, y])
      y += 80


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

    while run:
      screen.fill((0,0,0))
      screen.blit(background,(0,0))  #���ȭ�� ����
      screen.blit(startImg,(200,370))  #���۹�ư ǥ��
      screen.blit(rankingImg,(200,490))  #��ŷ��ư ǥ��
      screen.blit(settingImg,(200,610))  #���ù�ư ǥ��
      screen.blit(quitImg,(200,730))   #�������ư ǥ��


      for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:  #Ŭ���� �����Ǿ�����, Ŭ�� ��ǥ�� ���� �Ѿ��
            mouse = pygame.mouse.get_pos()
            local = [0, 0]
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

mainmenu()
