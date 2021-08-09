n, m, k = map(int, input().split())
array = list(map(int, input().split()))

result = 0
count = m//(k+1)
array.sort(reverse=True)
result = (array[0] * count * k) + (array[1] * count) + (array[0] * (m%(k+1)))
print(result)