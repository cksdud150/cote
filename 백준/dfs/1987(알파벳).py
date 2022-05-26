import sys
# from collections import defaultdict
sys.setrecursionlimit(10000)

def dfs(i,j):
    flag = 0
    for ni,nj in [(i-1,j),(i,j-1),(i,j+1),(i+1,j)]:
        if 0 <= ni < r and 0 <= nj < c:
            char = ord(board[ni][nj]) - 65
            if alpha[char] == 0:
                alpha[char] = 1
                dfs(ni,nj)
                alpha[char] = 0
            else:
                flag += 1
        else:
            flag += 1
        if flag == 4:
            count[i][j] = max(sum(alpha),count[i][j])
                
                
input = sys.stdin.readline
r,c = map(int,input().split())
alpha = [0]*26 # 어떤 알파벳 지나는지 저장
board  = [input().rstrip() for _ in range(r)]
count = [[0]*c for _ in range(r)] # 각 칸마다 최대 알파벳 수 저장하는 2차원배열
alpha[ord(board[0][0])-65] = 1
dfs(0,0)
result = 1
for i in count:
    result = max(max(i),result)
print(result)