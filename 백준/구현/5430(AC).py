import sys

input = sys.stdin.readline

t = int(input())
result = []

for _ in range(t): # 맨 앞 혹은 맨 뒤만 없어진다는것이 포인트
    f = input().strip()
    n = int(input())
    ac = eval(input())
    ac = list(map(str,ac))
    
    start = 0
    end = n
    flag = 1
    
    for a in f:
        if a == 'R':
            flag *= -1
        else:
            if flag == 1:
                start += 1
            else:
                end -= 1
    
    if start > end:
        result.append('error')
    else:
        if flag == 1:
            result.append('['+','.join(ac[start:end])+']')
        else:
            result.append('['+','.join(reversed(ac[start:end]))+']')

for x in result:
    print(x)