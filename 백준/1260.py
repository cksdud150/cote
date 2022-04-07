import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int, input().split())
graph = [[0]*n for _ in range(n)]

for _ in range(m):
    x,y = map(int, input().split())
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

visit = [False]*n

bfs_list = []
bfs_list.append(v)
deq_bfs = deque()
deq_bfs.append(v-1)
visit[v-1] = True
while deq_bfs:
    now = deq_bfs.popleft()
    for i in range(n):
        if graph[now][i] == 1 and not visit[i]:
            deq_bfs.append(i)
            bfs_list.append(i+1)
            visit[i] = True

visit = [False]*n
dfs_list = []
deq_dfs = deque()
deq_dfs.append(v-1)

while deq_dfs:
    now = deq_dfs.pop()
    if visit[now] == False:
        visit[now] = True
        dfs_list.append(now+1)
    for i in range(n-1,-1,-1):
        if graph[now][i] == 1 and not visit[i]:
            deq_dfs.append(i)
    
print(' '.join(map(str,dfs_list)))
print(' '.join(map(str,bfs_list)))