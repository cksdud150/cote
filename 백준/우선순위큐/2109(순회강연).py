import sys
import heapq
input = sys.stdin.readline

n = int(input())
pd = [list(map(int,input().split())) for _ in range(n)]
pd.sort(key = lambda x:x[1]) # 기한이 짧은 순으로 정렬
h = [] 

for i in range(n):
    heapq.heappush(h, pd[i]) # 최소값을 뽑아냄
    if len(h) > pd[i][1]: # len() 은 사용되는 일자를 구하기 위함
        heapq.heappop(h)

print(sum([x[0] for x in h]))
        

