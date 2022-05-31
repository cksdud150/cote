import sys
input = sys.stdin.readline

n = int(input())
board = []
dic = {} # 같은 색상의 누적합
for i in range(n):
    c, s = map(int,input().split())
    board.append([i,c,s,0])
    dic[c] = 0

board.sort(key = lambda x : (x[2],x[1]))

dic[board[0][1]] = board[0][2]
total = [0]*(n) # 색상이 다른데 크기가 같은 경우때문에 배열로 설정
t = board[0][2] # 색상 상관없이 누적합
total[0] = 0
for i in range(1,n):
    c = board[i][1]
    s = board[i][2]
    if s == board[i-1][2]: #크기가 다른 경우에만 total 값을 t로 업데이트
        total[i] = total[i-1] 
    else:
        total[i] = t
    if s == board[i-1][2] and c == board[i-1][1]: # 색상 크기 같은경우 같은 값 설정
        board[i][3] = board[i-1][3]
    else:
        board[i][3] = total[i] - dic[c] # 여태까지의 누적합에 같은 색상 누적합을 빼서 계산
    t += s
    dic[c] += s
    
    
    
board.sort(key = lambda x:x[0])    

for x in board:
    print(x[3])