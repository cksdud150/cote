n,m = map(int, input().split())

data = []
for i in range(n):
  data.append(list(map(int, input().split())))

min = []
for i in range(n):
  data[i].sort()
  min.append(data[i][0])

min.sort()
print(min[n-1])
