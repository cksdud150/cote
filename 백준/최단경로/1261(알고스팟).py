import sys
import heapq
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(map(int,input().rstrip())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        board[i][j] -= 2

h = []
board[0][0] = 0
heapq.heappush(h,(board[0][0],0,0))

while h:
    v,x,y = heapq.heappop(h)
    for nx,ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == -1:
                board[nx][ny] = board[x][y] + 1
                heapq.heappush(h,(board[nx][ny],nx,ny))
            if board[nx][ny] == -2:
                board[nx][ny] = board[x][y]
                heapq.heappush(h,(board[nx][ny],nx,ny))
            else:
                continue

print(board[n-1][m-1])