import time


n = int(input())
start = time.time()
maximum = 1000000
prime = [1] * maximum

prime[0] = 0
prime[1] = 0
result = 1003001

for i in range(maximum):
    if prime[i] == 1:
        for j in range(2*i,maximum,i):
            if prime[j] == 1:
                prime[j] = 0
        if i >= n:
            if str(i) == ''.join(reversed(str(i))):
                result = i
                break

print(result)
end = time.time()
print(end - start)