def dfs(x,y):
    if board[y][x] == 1:
        board[y][x] = 0
        if 0 <= x+1 < n:
            dfs(x+1,y)
        if 0 <= y+1 < m:
            dfs(x,y+1)
        if 0 <= x-1 < n:
            dfs(x-1,y)
        if 0 <= y-1 < m:
            dfs(x,y-1)

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

t = int(input())
count = []

for i in range(t):
    temp = 0
    n,m,k = map(int,input().split())
    board = [[0]*n for i in range(m)]
    for j in range(k):
        x, y = map(int,input().split())
        board[y][x] = 1
    for x in range(n):
        for y in range(m):
            if board[y][x] == 1:
                temp += 1
                dfs(x,y)
    count.append(temp)

for c in count:
    print(c)
