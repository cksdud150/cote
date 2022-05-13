def drawrow(s, onoff):
    if onoff:
        print(' '+'-'*s+' ',end = ' ')
    else:
        print(' '*(s+2),end = ' ')
        
def drawcol(s,type):
    if type == 1:
        print('|'+' '*(s+1),end = ' ')
    elif type == 0:
        print(' '*(s+1)+'|',end = ' ')
    elif type == 2:
        print('|'+' '*s+'|',end = ' ')
        
s, n = map(int, input().split())
n = list(map(int,str(n)))

dic = {1:[False,0,False,0,False],2:[True,0,True,1,True],3:[True,0,True,0,True],4:[False,2,True,0,False],5:[True,1,True,0,True],6:[True,1,True,2,True],7:[True,0,False,0,False],8:[True,2,True,2,True],9:[True,2,True,0,True],0:[True,2,False,2,True]}


for i in range(5):
    if i % 2 == 1:
        for _ in range(s):
            for j in n:
                drawcol(s,dic[j][i])
            print()
    else:
        for j in n:
            drawrow(s,dic[j][i])
        print()        

        