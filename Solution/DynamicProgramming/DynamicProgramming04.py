n, m = map(int, input().split())

array =[]
for i in range(n):
    array.append(int(input()))

d = [1000000] * 10001


for i in range(m+1):
    for k in array:
        d[k] = 1
        if i >= k:
            d[i] = min(d[i], d[i-k]+1)

if d[m] == 1000000:
    print(-1)
else:
    print(d[m])