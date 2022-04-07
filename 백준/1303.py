import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(m)]
result = {'W':0,'B':0}

def bfs(i,j):
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]
  deq = deque()
  k = board[i][j]
  board[i][j] = 0
  v = 0
  deq.append((i,j))
  while deq:
    i,j = deq.popleft()
    v += 1
    for idx in range(4):
      ni = i+dx[idx]
      nj = j+dy[idx]
      if 0 <= ni < m and 0 <= nj < n:
        if board[ni][nj] == k:
          board[ni][nj] = 0
          deq.append((ni,nj))
  return(k,v)

for i in range(m):
  for j in range(n):
    if board[i][j] != 0:
      k,v = bfs(i,j)
      result[k] += v ** 2

print(result['W'],result['B'])
      