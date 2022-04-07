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
    if 0 <= i < n and 0 <= j < m:
      if board[i][j] == 0:
        board[i][j] = 1
        queue.append((i+1,j))
        queue.append((i,j+1))
        queue.append((i,j-1))
        queue.append((i-1,j))

for i in range(n):
  for j in range(m):
    if board[i][j] == 0:
      bfs(i,j)
      count += 1
      
print(count)