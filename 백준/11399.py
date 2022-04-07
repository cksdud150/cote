n = int(input())
p = input()
p = [int(x) for x in p.split()]
p.sort()
sum = 0
for i in range(n):
    sum += p[i] * (n-i)
print(sum)