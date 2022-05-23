import pygame
import sys
import random
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((540, 725))
mainscreen = pygame.image.load("mainscreen.jpg")
pygame.display.set_caption("2048 game by Class101")
clock = pygame.time.Clock()

gamestartRec = pygame.Rect(146, 549, 256, 102)  #mainmenu의 시작버튼 범위
ranking_restartRec = pygame.Rect(242, 660, 132, 42)  #ranking의 재시작버튼 범위
ranking_quitRec = pygame.Rect(387, 660, 132, 42)  #ranking의 메인으로 나가기버튼 범위
gamestart_undoRec = pygame.Rect(367, 128, 54, 54)  #gamestart의 재시작 버튼
gamestart_settingRec = pygame.Rect(457, 128, 54, 54)  #gamestart의 세팅 버튼
gamestart_rankingboardRec = pygame.Rect(435, 71, 68, 32)

main1 = False     #mainscreen의 게임 스타트 키
ranking1 = False     #ranking의 재시작 키
ranking2 = False     #ranking의 메인으로 나가기 키
gamestart1 = False     #gamestart의 undo 키
gamestart2 = False     #gamestart의 설정 키
gamestart3 = False     #임시버튼!!! gamestart에서 랭킹보드로 가는 키

screen.fill((0,0,0))
screen.blit(mainscreen,(0,0))  #배경화면 설정

BLACK = (0, 0, 0)     #검정색 RGB 지정

#----------------------------------------------------------------------------------------------
#--------------------------gamestart를 위한 함수-----------------------------------------------

def gamestart():
    click_pos_gamestart = None
    global gamestart1     #gamestart의 undo 키
    global gamestart2     #gamestart의 설정 키
    global gamestart3     #임시버튼!!! gamestart에서 랭킹보드로 가는 키
    global main1      #main의 gamestart로 진입하기 위한 키, gamestart에서 빠져나갈 시 False로 변경
    print("gamestart")

    gamescreen = pygame.image.load("gamescreen.jpg")
    screen.blit(gamescreen,(0,0))  #게임화면 설정

    if event.type == pygame.MOUSEBUTTONUP:
       click_pos_gamestart = pygame.mouse.get_pos()
       print(click_pos_gamestart)

    if click_pos_gamestart:
      check_buttons_gamestart(click_pos_gamestart)

    if gamestart1:
        main1 = False     #gamestart에서 벗어날 시 False로 바꿔주어 추후 gamestart로 재진입이 가능하도록 한다
        gamestart1 = False
        undo()

    elif gamestart2:
        main1 = False     #gamestart에서 벗어날 시 False로 바꿔주어 추후 gamestart로 재진입이 가능하도록 한다
        gamestart2 = False
        setting()

    elif gamestart3:
        main1 = False
        gamestart3 = False
        ranking()

    

def check_buttons_gamestart(pos):
    global gamestart1
    global gamestart2
    global gamestart3

    if gamestart_undoRec.collidepoint(pos):
        gamestart1 = True

    elif gamestart_settingRec.collidepoint(pos):
        gamestart2 = True

    elif gamestart_rankingboardRec.collidepoint(pos):
        gamestart3 = True

def 2048_init():
    

#----------------------------------------------------------------------------------------------
#--------------------------undo을 위한 함수----------------------------------------------------

def undo():
    return

#----------------------------------------------------------------------------------------------
#--------------------------ranking을 위한 함수-------------------------------------------------

def ranking():
  click_pos_ranking = None
  global ranking1     #ranking의 재시작 키
  global ranking2     #ranking의 메인으로 나가기 키
  global main2      #main의 ranking으로 진입하기 위한 키, ranking에서 빠져나갈 시 False로 변경

  print("ranking")

  rankingboard = pygame.image.load("rankingscreen.png")
  screen.blit(rankingboard,(0,0))  #랭킹화면 설정

  board = open("ranking.txt", "r")     #순위표 open
    
  rankinglist = []     #순위를 담을 리스트 생성, 형식: ['이름', '점수']

  while True:
      line = board.readline()     #txt파일에서 한 줄씩 읽어오기

      if not line:     #txt 파일에서 읽어올 것이 없어, line이 비었다면, 중단
          break

      line = line.split()     #['이름 점수'] 형태를 ['이름', '점수'] 형태로 쪼개기
      rankinglist.append(line)     #rankinglist에 삽입
      
  board.close()     #txt파일 닫기
  
  y = 250     #텍스트가 출력될 y좌표, x는 변화가 없으므로 아래 반복문에서는 상수로 직접 입력
  for i in range(5):     #텍스트 출력
      myFont = pygame.font.SysFont( "arial", 30, True, False)
      name = myFont.render(rankinglist[i][0], True, BLACK)
      score = myFont.render(rankinglist[i][1], True, BLACK)

      screen.blit(name, [210, y])
      screen.blit(score, [340, y])
      y += 68

  if event.type == pygame.MOUSEBUTTONUP:
       click_pos_ranking = pygame.mouse.get_pos()
       print(click_pos_ranking)

  if click_pos_ranking:
      check_buttons_ranking(click_pos_ranking)

  if ranking1:
      main2 = False     #ranking으로 오기 위한 mainmenu의 버튼 key 초기화
      ranking1 = False
      gamestart()

  elif ranking2:
      main2 = False     #ranking으로 오기 위한 mainmenu의 버튼 key 초기화
      ranking2 = False

def check_buttons_ranking(pos):     #ranking에서 클릭한 위치에 따라 기능 실행
  global ranking1     #ranking의 재시작 키
  global ranking2     #ranking의 메인으로 나가기 키
  if ranking_restartRec.collidepoint(pos):
      ranking1 = True

  elif ranking_quitRec.collidepoint(pos):
      ranking2 = True

#----------------------------------------------------------------------------------------------
#--------------------------setting을 위한 함수-------------------------------------------------
 
def setting():
    print("setting")

#----------------------------------------------------------------------------------------------
#--------------------------quit을 위한 함수----------------------------------------------------

def quit():
    pygame.quit()
    sys.exit()

#----------------------------------------------------------------------------------------------
#--------------------------실행하는 While문, mainscreen 관련-----------------------------------
    
def mainmenu():
    print("mainmenu")
    screen.fill((0,0,0))
    screen.blit(mainscreen,(0,0))  #배경화면 설정

def check_buttons_main(pos):     #mainmenu에서 클릭한 위치에 따라 기능 실행
  global main1    #게임 스타트 키

  if gamestartRec.collidepoint(pos):
    main1 = True

run = True

while run:
    click_pos = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONUP:  #클릭이 감지되었을때, 클릭 좌표에 따라 넘어간다
            click_pos = pygame.mouse.get_pos()
            print(click_pos)

        if main1:     #게임 스타트 키
            gamestart()

        if click_pos:
            check_buttons_main(click_pos)

        pygame.display.update()
        clock.tick(30)

pygame.quit()

