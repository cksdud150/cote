n = list(map(int,input()))
n.sort(reverse = True)

if n[len(n)-1] == 0:
    if sum(n) % 3 == 0:
        print(''.join(map(str,n)))
    else:
        print(-1)
else:
    print(-1)