import sys
import heapq
import math
from itertools import combinations

input = sys.stdin.readline
INF = int(1e9)

# def is_prime(x):
#     for i in range(2,x):
#         if x % i == 0:
#             return False
#     return True
is_prime = [True]*9000
is_prime[0] = False
is_prime[1] = False
for i in range(2,int(9000**0.5)):
    if is_prime[i]:
        for j in range(i+i,9000,i):
            is_prime[j] = False
        # z = 2
        # y = i*z
        # while y < 9000:
        #     is_prime[y] = False
        #     z += 1
        #     y *= z
        

x_start, y_start, x_end, y_end = map(int,input().split())
x_y = [(x_start,y_start)]
n = int(input())
for _ in range(n):
    x_y.append(tuple(map(int,input().split())))
x_y.append((x_end,y_end))
graph = [[] for _ in range(n+2)]
distance = [INF]*(n+2)

for i,j in combinations(range(n+2),2):
    dist = int(math.dist(x_y[i],x_y[j]))
    if is_prime[dist]:
        graph[i].append((j,dist))
        graph[j].append((i,dist))
# for i in range(n+2):
#     for j in range(i):
#         if i == j:
#             continue
#         x = x_y[i][0]-x_y[j][0]
#         y = x_y[i][1]-x_y[j][1]
#         dist = int(math.sqrt(x*x + y*y))
#         if is_prime(dist):
#             graph[i].append((j,dist))
#             graph[j].append((i,dist))

h = []
heapq.heappush(h,(0,0))
distance[0] = 0

while h:
    dist, now = heapq.heappop(h)
    if dist > distance[now]:
        continue
    for mid in graph[now]:
        cost = dist + mid[1]
        if distance[mid[0]] > cost:
            distance[mid[0]] = cost
            heapq.heappush(h,(cost,mid[0]))

if distance[n+1] == INF:
    print(-1)
else:
    print(distance[n+1])
                
        
