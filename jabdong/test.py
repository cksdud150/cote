from collections import deque

def solution(n, paths, gates, summits):
    answer = []
    board = [[10000000]*(n+1) for _ in range(n+1)]
    for i,j,cost in paths:
        board[i][j] = cost    
    intensity = []
    for i in summits:
        intensity.append((dfs(gates,summits,i,board,False,0),i))

    return intensity.sort(key = lambda x: (-x[0],x[1]))[0]

def dfs(gates,summits,i,board,flag,maxi):
    if flag:
        return maxi
    if i in gates:
        flag = True
    if i in summits:
        return maxi
    j = board[i].index(min(board[i]))
    maxi = max(maxi,board[i][j])
    maxi = dfs(gates,summits,j,board,flag,maxi)
    if flag:
        return maxi
    else:
        board[i][j] = 100000
        j = board[i].index(min(board[i]))
        max(maxi,board[i][j])
        
