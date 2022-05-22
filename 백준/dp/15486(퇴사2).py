import sys
input = sys.stdin.readline

n = int(input())
tp = [[]]
for _ in range(n):
    tp.append(list(map(int,input().split())))
total = [0]*(n+2)

for i in range(1,n+1):
    total[i] = max(total[i],total[i-1])
    time = tp[i][0]
    if i+time > n+1:
        continue
    total[i+time] = max(total[i] + tp[i][1],total[i+time])
print(max(total))
