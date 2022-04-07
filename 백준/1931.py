import sys
myInput = sys.stdin.readline
n = int(myInput())
all = []
for i in range(n):
    temp = myInput()
    s,e = temp.split()
    all.append([int(s),int(e)])
all.sort(key=lambda x: (x[1],x[0]))
order = [all[0]]
j = 0
for i in range(1,n):
    if order[j][1] <= all[i][0]:
        order.append(all[i])
        j += 1
print(len(order))