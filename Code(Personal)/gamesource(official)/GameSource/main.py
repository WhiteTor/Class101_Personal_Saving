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

gamestartRec = pygame.Rect(200, 370, 236, 100)
rankingRec = pygame.Rect(200, 490, 236, 100)
settingRec = pygame.Rect(200, 610, 236, 100)
quitRec = pygame.Rect(200, 730, 236, 100)
ranking_backRec = pygame.Rect(10, 10, 150, 175)

run = True
set1 = False     #게임 스타트 키
set2 = False     #랭킹 키
set3 = False     #세팅 키
set4 = False     #종료 키

def check_buttons(pos):
  global set1
  global set2
  global set3
  global set4
  if gamestartRec.collidepoint(pos):
    set1 == True

  elif rankingRec.collidepoint(pos):
    set2 == True

  elif settingRec.collidepoint(pos):
    set3 == True

  elif quitRec.collidepoint(pos):
    set4 == True


def ranking():
  global run
  print("ranking")

  rankingboard = pygame.image.load("rankingboard.png")
  screen.blit(rankingboard,(0,0))  #랭킹화면 설정
  screen.blit(backImg,(10,10))
  if event.type == pygame.MOUSEBUTTONUP:
      if ranking_backRec.collidepoint(pygame.mouse.get_pos()):
        mainmenu()

def quit():
    pygame.quit()
    sys.exit()

def mainmenu():
    global run
    global event
    click_pos = None

    while run:
      
      screen.fill((0,0,0))
      screen.blit(background,(0,0))  #배경화면 설정
      screen.blit(startImg,(200,370))  #시작버튼 표시
      screen.blit(rankingImg,(200,490))  #랭킹버튼 표시
      screen.blit(settingImg,(200,610))  #세팅버튼 표시
      screen.blit(quitImg,(200,730))   #나가기버튼 표시


      for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONUP:  #클릭이 감지되었을때, 클릭 좌표에 따라 넘어간다
            click_pos = pygame.mouse.get_pos()
            print(click_pos)
            
        if set1:
          gamestart()
        elif set2:
          ranking()
        elif set3:
          setting()
        elif set4:
          quit()

        if click_pos:
            check_buttons(click_pos)

        pygame.display.update()
        clock.tick(30)


mainmenu()