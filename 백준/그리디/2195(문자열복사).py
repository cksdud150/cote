s = input()
p = input()

n_p = len(p)
n = 0
result = 1

for i in range(n_p):
    x = s.find(p[i-n:i+1])
    if x != -1:
        n += 1
    else:
        n = 1
        result += 1

print(result)