import sys

n,m = map(int,input().split())

miro = [list(map(int,sys.stdin.readline().rstrip())) for i in range(n)]
visit = [[0]*m for i in range(n)]
count = 0

def dfs(i,j):
  global count
  if not (0 <= i < n and 0 <= j < m):
    return
  if visit[i][j] == 1:
    return
  if miro[i][j] == 0:
    return
  visit[i][j] = 1
  count += 1
  if i == n-1 and j == m-1:
    print(count)
    return
  dfs(i,j+1)
  dfs(i+1,j)
  dfs(i-1,j)
  dfs(i,j-1)
  return
  
dfs(0,0)
