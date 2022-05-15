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

def ranking():
  print("ranking")

  rankingboard = pygame.image.load("rankingboard.png")
  screen.blit(rankingboard,(0,0))  #��ŷȭ�� ����
  screen.blit(backImg,(10,10))
  board = open("ranking.txt", "r")
    
  rankinglist = []

  while True:
      line = board.readline()
      line = line.split()
      rankinglist.append(line)
      if not line:
          break

  board.close()
  
  BLACK = (0, 0, 0)
  font = pygame.font.SysFont("arial", 30, True, True)
  x = 200
  y = 350
  for i in range(5):
      for j in range(2):
          text = font.render(str(rankinglist[i][j]), True, BLACK)

          screen.bilt(text,(x, y))
          y += 100


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
            if 436 > mouse[0] > 200 and 470 > mouse[1] > 370:
                gamestart()

            elif 436 > mouse[0] > 200 and 590 > mouse[1] > 490:
                ranking()

            elif 436 > mouse[0] > 200 and 710 > mouse[1] > 610:
                setting()

            elif 436 > mouse[0] > 200 and 830 > mouse[1] > 730:
                quit()

        pygame.display.update()
        clock.tick(30)

mainmenu()
