n = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
x = 1
y = 1
array = list(input().split())

for i in array:
    a = y
    b = x
    if i == "L":
        a = y + dx[1]
    elif i == "R":
        a = y + dx[0]
    elif i == "U":
        b = x + dy[3]
    elif i == "D":
        b = x + dy[2]
    if a < 1 or a > n or b < 1 or b > n:
        continue
    x = b
    y = a

print(x, y)