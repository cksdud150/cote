import heapq

n = int(input())
dasom = int(input())
vote = []
result = 0

for _ in range(n-1):
    heapq.heappush(vote,-int(input()))

now = 0
try:
    now = -heapq.heappop(vote)
except:
    pass
while dasom <= now:
    now -= 1
    heapq.heappush(vote,-int(now))
    dasom += 1
    result += 1
    now = -heapq.heappop(vote)

print(result)