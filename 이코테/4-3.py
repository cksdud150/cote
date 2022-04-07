n,m = map(int,input().split())

x,y,d = map(int,input().split())

dx = (0,1,0,-1)
dy = (1,0,-1,0)

count = 1

game_map = []
for i in range(n):
  game_map.append(list(map(int,input().split())))

while True:
  print(y,x)
  game_map[y][x] = 2
  for j in range(4):
    d = (d - 1) % 4
    if game_map[dy[d]+y][dx[d]+x] == 0:
      y = dy[d] + y
      x = dx[d] + x
      game_map[y][x] = 2
      count += 1
      break
    if j == 3:
      y = y - dy[d]
      x = x - dx[d]
  if game_map[y][x] == 1:
    break

print(count)