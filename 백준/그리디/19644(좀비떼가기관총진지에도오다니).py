import sys
from collections import deque

input = sys.stdin.readline

l = int(input())
ml, mk = map(int,input().split())
c = int(input())
zombie = [int(input()) for _ in range(l)]
zombie = deque(zombie)
gun = deque([(i+1)*mk for i in range(ml)]) # 총이 주는 데미지 배열
bomb = deque([0]*ml) # 폭탄을 사용한적이 있는지 체크하는 배열
result = 'YES'

n_bomb = 0 # 현재 상태에서 폭탄이 몇개가 사용되는지

for _ in range(l):
    g = gun.popleft()
    now = zombie.popleft() # 좀비의 체력
    if now > g - n_bomb*mk: # 총이 주는 데미지 - 폭탄이 사용된 이력, 좀비체력이 총 데미지보다 높은경우 폭탄 사용
        c -= 1                
        bomb.append(1)
        n_bomb += 1
        if c == -1:
            result = 'NO'
            break
    else:
        bomb.append(0)
    n_bomb -= bomb.popleft() # 폭탄사용한 이력에 따라 폭탄 갯수 업데이트
    gun.append(mk*ml) # 총이 주는 최대 데미지를 추가

print(result)