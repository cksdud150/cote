n,k = map(int,input().split())

prime = [1]*(n+1) 
count = 0
flag = False
result = 0
for i in range(2,n+1):
    if prime[i] == 1:
        for j in range(i,n+1,i):
            if j > n:
                break
            if prime[j] == 1:
                count += 1
                prime[j] = 0
            if count == k:
                flag = True
                result = j
                break
    if flag:
        break

print(result)