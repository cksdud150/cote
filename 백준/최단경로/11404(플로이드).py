import sys
INF = int(10e9)

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [list(map(int,input().split())) for _ in range(m)]
distance = [[INF]*(n+1) for _ in range(n+1)]
for i,j,d in graph:
    distance[i][j] = min(d,distance[i][j])

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            distance[i][j] = min(distance[i][j],distance[i][k]+distance[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if distance[i][j] == INF or i == j:
            print(0,end = ' ')
        else:
            print(distance[i][j],end = ' ')
    print()
    