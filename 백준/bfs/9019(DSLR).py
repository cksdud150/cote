from collections import deque
def L(x):
    a1 = x // 1000
    x = (x - a1*1000)*10 + a1
    return x

def R(x):
    a4 = x % 10
    x = (x // 10) + a4 * 1000
    return x

def D(x):
    x = x*2
    if x > 9999:
        x = x % 10000
    return x

def S(x):
    x -= 1
    if x == -1:
        x = 9999
    return x



t = int(input()) 
fun = [D,S,L,R] #함수 리스트
fun_str = ['D','S','L','R'] 
aa = []
bb = []
results = []

for _ in range(t):
    a,b = map(int,input().split())
    aa.append(a)
    bb.append(b)

for j in range(t):
    a = aa[j]
    b = bb[j]
    result = ['']*10000

    deq = deque()
    deq.append(a)
    
    while deq: #bfs
        now = deq.popleft()
        if now == b:
            break
        for i in range(4):
            x = fun[i](now)
            if result[x] == '' and x != a:
                result[x] = result[now] + fun_str[i]
                deq.append(x)
                
    results.append(result[b])
    
for j in range(t):
    print(results[j])
