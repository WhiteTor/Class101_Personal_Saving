def saving_best_score(user_score, user_name):

    board = open("ranking.txt", "r")     #순위표 open
    rankinglist = []     #순위를 담을 리스트 생성, 형식: ['이름', '점수']
    comparescore = []     #순위를 담을 리스트 생성, 단 점수만 담는다.
    changedlist = []     #순위가 변경될 경우 변경된 순위를 담아놓는 리스트. 이를 txt파일에 적용한다
    while True:
        text = board.readline()     #txt파일에서 한 줄씩 읽어오기
        if not text:     #txt 파일에서 읽어올 것이 없어, text가 비었다면, 중단
            break
        text = text.split()     #['이름 점수'] 형태를 ['이름', '점수'] 형태로 쪼개기
        rankinglist.append(text)     #rankinglist에 삽입, 이 리스트는 이름과 점수를 모두 저장한다
        comparescore.append(text[1])     #comparescore에 삽입, 이 리스트는 점수만을 저장한다
    
    
    board.close()     #txt파일 닫기

    comparescore = list(map(int, comparescore))

    user_new_ranking = None

    rankingchangeKey = False

    for i in range(5):
        if user_score > comparescore[i]:
            rankinglist[i][0] = user_name
            rankinglist[i][1] = user_score
            rankingchangeKey = True
            break
    
    if rankingchangeKey:
        board = open("ranking.txt", "w")
        for i in range(5):
            temp = []
            for j in range(2):
                temp.append(rankinglist[i][j])
            temp = list(map(str, temp))
            changedtemp = " ".join(temp)
            board.write(changedtemp + '\n')
        
        board.close()


user_score = 48000
user_name = 'Kim'
saving_best_score(user_score, user_name)
