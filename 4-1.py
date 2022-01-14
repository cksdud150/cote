n = int(input())
move = input().split()

site = [1,1]

for i in range(len(move)):
  
  if move[i] == 'L':
    if site[0] == 1:
      continue
    else: site[0] -= 1
  elif move[i] == 'U':
    if site[1] == 1:
      continue
    else: site[1] -= 1
  elif move[i] == 'R':
    if site[0] == n:
      continue
    else: site[0] += 1
  elif move[i] == 'D':
    if site[1] == n:
      continue
    else: site[1] += 1
  print(site)

print(site[1],site[0])