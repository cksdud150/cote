import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int,input().rstrip())) for _ in range(n)]

que = deque()
que.append((0,0))

while que:
    x,y = que.popleft()
    for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 1:
                que.append((nx,ny))
                board[nx][ny] = board[x][y] + 1

print(board[n-1][m-1])