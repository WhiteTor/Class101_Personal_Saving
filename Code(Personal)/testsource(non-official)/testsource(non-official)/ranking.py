board = open("ranking.txt", "r")

rankinglist = []

while True:
    line = board.readline()
    line = line.split()
    rankinglist.append(line)
    if not line:
        break

board.close()

for i in range(5):
    for j in range(2):
        print(rankinglist[i][j])