import heapq

n = int(input())
dasom = int(input())
vote = []
result = 0

for _ in range(n-1):
    heapq.heappush(vote,-int(input()))

now = 0
try:
    now = -heapq.heappop(vote) # 최대값을 계속 출력
except:
    pass
while dasom <= now: # 다솜이 최대값보다 커지면 반복문 멈춤
    now -= 1
    heapq.heappush(vote,-int(now))
    dasom += 1
    result += 1
    now = -heapq.heappop(vote)

print(result)