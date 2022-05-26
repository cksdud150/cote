import sys
input = sys.stdin.readline

n,k = map(int,input().split())
result = [[0]*(k+1) for _ in range(n+1)]

w_v = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n+1):
    w,v = w_v[i-1]
    for j in range(1,k+1):
        if j >= w:
            result[i][j] = max(result[i-1][j-w]+v,result[i-1][j])
        else:
            result[i][j] = result[i-1][j]

print(result[n][k])