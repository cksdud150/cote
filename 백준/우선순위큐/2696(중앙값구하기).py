import sys
import heapq

input = sys.stdin.readline

t = int(input())
n = []
tndufs = []

for j in range(t): # 데이터 입력
    n.append(int(input()))
    tnduf = []
    for _ in range(n[j]//10+1):
        tnduf.extend(list(map(int,input().split())))
    tndufs.append(tnduf)

results = [] 

for j in range(t):
    result = []
    big = [] # 중간값 보다 큰 값을 넣을 우선순위큐
    n_big = 0 # 길이를 저장
    small = [] # 중간값 보다 작은 값을 넣을 우선순위큐
    n_small = 0 # 길이를 저장
    tnduf = tndufs[j]
    middle = tnduf[0]
    result.append(middle)
    for i in range(1,n[j]):
        if tnduf[i] > middle:
            heapq.heappush(big,tnduf[i])
            n_big += 1
        else:
            heapq.heappush(small,-tnduf[i])
            n_small += 1
        if i % 2 == 0: # 중간값을 업데이트하는 과정
            if n_big == n_small:
                pass
            elif n_big > n_small:
                heapq.heappush(small,-middle)
                middle = heapq.heappop(big)
            else:
                heapq.heappush(big,middle)
                middle = -heapq.heappop(small)
            n_big = 0
            n_small = 0
            result.append(middle)
    results.append(result)

for j in range(t):
    m = int((n[j]+1)/2)
    print(m)
    for k in range(m):
        if k % 10  == 0 and k != 0:
            print()
        print(results[j][k], end = ' ')
    print()
