import sys
# import heapq # 원래는 최소 힙 써서 했지만 시간초과가 나서 QUEUE를 두개 이용하는 방향으로
from collections import deque

input = sys.stdin.readline

r,c = map(int,input().split())
board = [[-1]*c for _ in range(r)]
duck = []
deq = deque()
deq2 = deque()

for i in range(r):
    temp = input().rstrip()
    for j in range(c):
        if temp[j] == 'X':
            pass
        elif temp[j] == 'L':
            duck.append((i,j))
            deq.append([i,j])
            board[i][j] = 0
        else:
            deq.append([i,j])
            board[i][j] = 0
v = 1

while True:
    if not deq:
        if not deq2:
            break
        else:
            v += 1
            deq = deq2
            deq2 = deque()
    i,j = deq.pop()
    for ni,nj in [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]:
        if 0 <= ni < r and 0 <= nj < c:
            if board[ni][nj] == -1:
                board[ni][nj] = v
                deq2.append([ni,nj])

result = 0
flag = 0
deq.append([duck[0][0], duck[0][1]])

while True:
    if flag:
        break
    if not deq:
        result += 1
        deq = deq2
        deq2 = deque()
    i,j = deq.pop()
    board[i][j] = -1
    for ni,nj in [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]:
        if 0 <= ni < r and 0 <= nj < c:
            if board[ni][nj] == -1:
                pass
            elif board[ni][nj] <= result:
                deq.append([ni,nj])
            else:
                deq2.append([ni,nj])
            if ni == duck[1][0] and nj == duck[1][1]:
                flag = 1

print(result)
