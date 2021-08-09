n, k =map(int, (input().split()))
array_a = map(int, input().split())
array_b = map(int, input().split())
array_a = sorted(array_a)
array_b = sorted(array_b, reverse=True)

for i in range(k):
    if array_a[i] < array_b[i]:
        array_a[i], array_b[i] = array_b[i], array_a[i]

print(sum(array_a))