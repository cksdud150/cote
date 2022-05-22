import sys
# import heapq
from collections import deque

input = sys.stdin.readline
INF = int(1e7)
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
result = [[INF]*n for _ in range(n)]
result[0][0] = 0
# h = deque()
# # heapq.heappush(h,(result[0][0],0,0))
# h.append((0,0))
# while h:
#     # print(h)
#     # cost,i,j = heapq.heappop(h)
#     # if i == n-1 and j == n-1:
#         # break
#     i,j = h.popleft()
#     for ni, nj in [(i+1,j),(i,j+1)]:
#         if ni >= n or nj >= n:
#             continue
#         # if result[ni][nj] < cost:
#         #     continue
#         if board[i][j] > board[ni][nj]:
#             result[ni][nj] = min(result[i][j],result[ni][nj])
#         else:
#             result[ni][nj] = min(result[i][j] + board[ni][nj] - board[i][j] + 1,result[ni][nj])
#         # heapq.heappush(h,(result[ni][nj],ni,nj))
#         h.append((ni,nj))
for i in range(n):
    for j in range(n):
        for ni, nj in [(i+1,j),(i,j+1)]:
            if ni >= n or nj >= n:
                continue
            if board[i][j] > board[ni][nj]:
                result[ni][nj] = min(result[i][j],result[ni][nj])
            else:
                result[ni][nj] = min(result[i][j] + board[ni][nj] - board[i][j] + 1,result[ni][nj])

print(result[n-1][n-1])