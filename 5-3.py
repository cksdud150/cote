from collections import deque
import sys

n, m = map(int,input().split())
count = 0
board = []
for i in range(n):
  board.append(list(map(int,list(sys.stdin.readline().rstrip()))))

def bfs(i,j):
  global board
  queue = deque([(i,j)])
  while queue:
    i,j = queue.popleft()
    board[i][j] = 1
    if i+1 != n:
      if board[i+1][j] == 0:
        queue.append((i+1,j))
    if j+1 != m:
      if board[i][j+1] == 0:
        queue.append((i,j+1))
    if j-1 != -1:
      if board[i][j-1] == 0:
        queue.append((i,j-1))
    if i-1 != -1:
      if board[i-1][j] == 0:
        queue.append((i-1,j))

for i in range(n):
  for j in range(m):
    if board[i][j] == 0:
      bfs(i,j)
      count += 1
      
print(count)