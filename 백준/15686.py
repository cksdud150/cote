import sys
from itertools import combinations
input = sys.stdin.readline

def chickdis(house,chick):
    distance = 0
    for i in house:
        shortest = 1000
        for j in chick:
            now = abs(i[0] - j[0]) + abs(i[1] - j[1])
            if now < shortest:
                shortest = now
        distance += shortest
    return distance
       

n, m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
house = []
chick = []
minimum = 10000

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append((i,j))
        elif board[i][j] == 2:
            chick.append((i,j))


for ck in combinations(chick,m):
    distance = chickdis(house,ck)
    if distance < minimum:
        minimum = distance

print(minimum)