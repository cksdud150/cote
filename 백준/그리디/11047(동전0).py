import sys
input = sys.stdin.readline

n, k = list(map(int,input().split()))
coin = []
count = 0

for i in range(n):
    coin.append(int(input()))

coin.sort(reverse = True)

for j in coin:
    count += k // j
    k = k % j

print(count)    

