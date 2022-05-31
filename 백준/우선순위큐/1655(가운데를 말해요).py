import sys
import heapq

input = sys.stdin.readline

n = int(input())

big = []
n_big = 0
small = []
n_small = 0
middle = int(input())
result = [middle]
for _ in range(n-1):
    now = int(input())
    if now >= middle :
        heapq.heappush(big,now)
        n_big += 1
    else:
        heapq.heappush(small,-now)
        n_small += 1
    if n_small > n_big:
        heapq.heappush(big,middle)
        middle = -heapq.heappop(small)
        n_small -= 1
        n_big += 1
    elif n_small + 1 < n_big:
        heapq.heappush(small,-middle)
        middle = heapq.heappop(big)
        n_big -= 1
        n_small += 1
    result.append(middle)

for i in result:
    print(i)