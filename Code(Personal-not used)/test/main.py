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
  mouse = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()

  rankingboard = pygame.image.load("rankingboard.png")
  screen.blit(rankingboard,(0,0))  #랭킹화면 설정
  screen.blit(backImg,(10,10))
  if click[0]:
    if 160 > mouse[0] > 10 and 185 > mouse[1] > 10:
      mainmenu()

def quit():
    pygame.quit()
    sys.exit()

def mainmenu():
  global run
  while run:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))  #배경화면 설정
    screen.blit(startImg,(200,370))  #시작버튼 표시
    screen.blit(rankingImg,(200,490))  #랭킹버튼 표시
    screen.blit(settingImg,(200,610))  #세팅버튼 표시
    screen.blit(quitImg,(200,730))   #나가기버튼 표시


    for event in pygame.event.get():
      mouse = pygame.mouse.get_pos()
      click = pygame.mouse.get_pressed()
      if click[0]:  #클릭이 감지되었을때, 클릭 좌표에 따라 넘어간다
        if 436 > mouse[0] > 200 and 470 > mouse[1] > 370:
          gamestart()

        elif 436 > mouse[0] > 200 and 590 > mouse[1] > 490:
          ranking()

        elif 436 > mouse[0] > 200 and 710 > mouse[1] > 610:
          setting()

        elif 436 > mouse[0] > 200 and 830 > mouse[1] > 730:
          quit()
          
        else:
          mainmenu()

    pygame.display.update()
    clock.tick(30)

run = True

mainmenu()

