import sys
input = sys.stdin.readline

t = int(input())
counts = []
for __ in range(t):
    x_start, y_start, x_end, y_end = map(int,input().split())
    n = int(input())
    plant = [list(map(int,input().split())) for _ in range(n)]
    count = 0
    for x,y,r in plant:
        flag = 1
        if ((x_start - x)**2 + (y_start - y)**2) < r**2:
            count += flag
            flag = -1
        if ((x_end - x)**2 + (y_end - y)**2) < r**2:
            count += flag
    counts.append(count)

for i in counts:
    print(i)
            

