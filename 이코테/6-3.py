n = int(input())

student = [tuple(input().split()) for i in range(n)]

student.sort(key = lambda x: x[1])

for j in range(n):
  print(student[j][0], end = ' ')