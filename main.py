n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
first = num[n-1]
second = num[n-2]
result = 0
n // k

result += first * k * (m // (k+1))
result += second * (m //(k+1))
result += first * (m % (k+1))

print(result)