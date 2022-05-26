import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    x_y = [list(map(int,input().split())) for _ in range(n+2)]
    possible = [[0]*(n+2) for _ in range(n+2)]
    for i,j in combinations(range(n+2),2): # 갈수 있는지 체크
        flag = int(abs(x_y[i][0] - x_y[j][0]) + abs(x_y[i][1] - x_y[j][1]) <= 1000)
        possible[i][j] = flag
        possible[j][i] = flag)
    deq = deque()
    deq.append(0)
    visit = [False]*(n+2)
    while deq:
        now = deq.popleft()
        for i in range(n+2):
            if possible[now][i] == 1 and visit[i] == False:
                deq.append(i)
                visit[i] = True
    results.append('happy' if visit[n+1] else 'sad')    
    
print('\n'.join(results))