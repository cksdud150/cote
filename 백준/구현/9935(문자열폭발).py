string = input()
bomb = input()
n_bomb = len(bomb)
delete = [] # 삭제해야할 인덱스 저장용
idx = 0 # bomb랑 일치하는 인덱스 길이
idx_list = [] # 스택
temp = [] # bomb이랑 얼마나 일치하는지 저장하기 위함
result = ''

for i,s in enumerate(string):
    if s == bomb[idx]: # bomb랑 일치하는지를 계속 확인
        temp.append(i)
        if idx == n_bomb-1: # 최대 길이에 도달한 경우
            delete.extend(temp) 
            try:
                idx, temp = idx_list.pop() # 스택에서 팝
            except: # idx_list가 비어있는 경우
                idx = 0
                temp = []
        else:
            idx += 1
    elif s == bomb[0]: # 새로운 시작인경우
        idx_list.append([idx,temp]) # 기존 정보를 스택에 저장
        temp = [i]
        idx = 1
    else : # 아닌경우 전부 초기화
        idx_list = []
        idx = 0
        temp = []

delete.sort()
delete.append(-1)

j = 0
for i,s in enumerate(string):
    if i == delete[j]:
        j += 1
    else:
        result = result + s

print(result if result != '' else 'FRULA')