site = input()
column = ['a','b','c','d','e','f','g','h']
row = list(map(str,range(1,9)))

count = 8
for i in range(8):
  if column[i] == site[0]:
    for j in range(8):
      if row[j] == site[1]:
        if not (1 < i < 6) :
          count -= 2
        if not (1 < j < 6) :
          count -= 2
        if i == 0 or i == 7:
          count -= 1
        if j == 0 or j == 7:
          count -= 1

print(count)
