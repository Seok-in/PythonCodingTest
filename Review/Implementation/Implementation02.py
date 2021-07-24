n = int(input())
count = 0
for i in range(n+1):
    h = str(i)
    for j in range(60):
        m = str(j)
        for k in range(60):
            s = str(k)
            if '3' in h or '3' in m or '3' in s:
                count += 1
print(count)