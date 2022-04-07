n = int(input())

up_to_down = [int(input()) for i in range(n)]

up_to_down.sort(reverse = True)

print(*up_to_down)