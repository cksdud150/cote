import sys
import heapq
input = sys.stdin.readline

n = int(input())
pd = [list(map(int,input().split())) for _ in range(n)]
pd.sort(key = lambda x:x[1])
h = []

for i in range(n):
    heapq.heappush(h, pd[i])
    if len(h) > pd[i][1]:
        heapq.heappop(h)

print(sum([x[0] for x in h]))
        

