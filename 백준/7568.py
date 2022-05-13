import sys
input = sys.stdin.readline

n = int(input())
body = [list(map(int,input().split())) for _ in range(n)]

score = []

for i in range(n):
    count = 1
    for j in range(n):
        if body[j][0] > body[i][0]:
            if body[j][1] > body[i][1]:
                count += 1
    score.append(count)

for r in score:
    print(r,end = ' ')

