import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

n = int(input())
dic = defaultdict(list)
key = []
result = 0

for i in range(n):
    a,b = map(int,input().split())
    heapq.heappush(dic[b],-a)
    key.append(b)

key = list(set(key))
key.sort(reverse = True)

max = 0
j = key.pop()
for i in range(n):
    print(result)
    if n-i > j:
        j = key.pop()
        continue
    now = -heapq.heappop(dic[j])
    if max < now:
        result += now
        try:
            max = -heapq.heappop(dic[j])
        except IndexError:
            j = key.pop()
            max = 0
    else:
        result += max
        j = key.pop()

print(result)
