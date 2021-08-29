INF = int(1e9)
n, m = map(int, input().split())
array = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            array[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    array[a][b] = 1
    array[b][a] = 1

x, k = map(int, input().split())
for j in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            array[a][b] = min(array[a][b], array[a][j] + array[j][b])

distance = array[1][k] + array[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)