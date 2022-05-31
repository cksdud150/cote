import sys
import heapq
input = sys.stdin.readline
n = int(input())
card = [int(input()) for _ in range(n)]
card.sort()
result = 0

for _ in range(n-1): # 카드의 가장 작은 두값을 계속 더하는게 포인트
    x1 = heapq.heappop(card) 
    x2 = heapq.heappop(card)
    x3 = x1 + x2
    heapq.heappush(card,x3)
    result += x3

print(result)