n = int(input())
arr = [1]*10

for i in range(n-1):
    for j in range(10):
        arr[j] = sum(arr[j:10])


print(sum(arr)%10007)