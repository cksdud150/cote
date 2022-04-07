from collections import deque

n,k = map(int,input().split())
que = deque()
que.append(n)
now = n
second = [0]*100001
second[now] = 1
count = [0]*100001
count[now] = 1
flag = 0
while que:
    now = que.popleft()
    if flag == 0 or second[now] == second[k] - 1:
        for next in [now+1,now-1,now*2]:
            if next < 0 or next > 100000:
                continue
            if second[next] == 0:            
                que.append(next)
                second[next] = second[now] + 1
                count[next] = count[now]
            elif second[next] == second[now] + 1:
                count[next] += count[now]
            if next == k:
                flag = 1
print(second[k]-1)
print(count[k])
