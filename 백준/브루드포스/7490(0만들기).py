from itertools import product

t = int(input())
for _ in range(t):
    n = int(input())
    operation = ['','+','-']
    num = 0
    formula = ['']*(2*n-1)
    result = []
    
    oper_list = product(operation,repeat = n-1) # 중복 순열 생성
    for i in range(n):
        formula[2*i] = str(i+1) # 숫자 입력
    
    for oper in oper_list:
        for i in range(n-1):
            formula[2*i+1] = oper[i] # 연산자 입력
        if eval(''.join(formula)) == 0: # 0이 되면 result에 append
            result.append(formula.copy())
    
    for r in result:
        print(''.join([x if x != '' else ' ' for x in r]))
    print()
