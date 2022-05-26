def dfs(x,y):
    global temp
    if 0 <= x < n and 0 <= y < n:
        if board[x][y] == 1:
            temp += 1
            board[x][y] = 0
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x-1,y)
            dfs(x,y-1)

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().rstrip())) for i in range(n)]
count = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            temp = 0
            dfs(i,j)
            count.append(temp)

print(len(count))
count.sort()
for i in count:
  print(i)



