n = int(input())

arr = [0,1,1]
for i in range(3,n): # i 는 인덱스
  j = i+1 # 실제 숫자
  temp = []
  if j % 3 == 0:
    temp.append(arr[j//3-1]+1)
  if j % 2 == 0:
    temp.append(arr[j//2-1]+1)
  temp.append(arr[i-1]+1)
  arr.append(min(temp))
print(arr[n-1])