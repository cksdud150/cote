# n = int(input())

# arr = [0,1,1]
# for i in range(3,n): # i 는 인덱스
#   j = i+1 # 실제 숫자
#   temp = []
#   if j % 3 == 0:
#     temp.append(arr[j//3-1]+1)
#   if j % 2 == 0:
#     temp.append(arr[j//2-1]+1)
#   temp.append(arr[i-1]+1)
#   arr.append(min(temp))
# print(arr[n-1])

##############################

# n = int(input())

# arr = [0,1,2]
# for i in range(3,n+1):
#   arr.append(arr[i-2] + arr[i-1])

# print(arr[n]%10007)

###############################

# n = int(input())

# arr = [0,1,3]
# for i in range(3,n+1):
#   arr.append(arr[i-2]*2 + arr[i-1])

# print(arr[n]%10007)

##################################33
import sys

n = int(input())
tp = []
cost = []

for i in range(n):
  tp.append(list(map(int,list(sys.stdin.readline().split()))))

for i in range(n):
  cost[i] 


