import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


n, m = map(int,input().split())
visible = list(map(int,input().split()))
visible[n-1] = 0
graph = [[] for _ in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


h = []
heapq.heappush(h,(0,0))
distance = [INF]*n
distance[0] = 0

while h:
    dist, now = heapq.heappop(h)
    if dist > distance[now]:
        continue
    for i,j in graph[now]:
        if j + dist < distance[i] and not visible[i]:
            distance[i] = j + dist
            heapq.heappush(h,(j + dist,i))

if distance[n-1] == INF:
    print(-1)
else:
    print(distance[n-1])