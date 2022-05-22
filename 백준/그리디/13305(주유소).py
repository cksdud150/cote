n = int(input())
d = [int(x) for x in input().split()]
p = [int(x) for x in input().split()]
low = p[0]
sum = 0
for i in range(n-1):
    if low > p[i]:
        low = p[i]
    sum += low*d[i]
print(sum)