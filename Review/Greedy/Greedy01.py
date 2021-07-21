n = int(input())
array = [500, 100, 50, 10]
result = 0
for i in array:
    if n >= i :
        result += (n // i)
        n %= i


print(result)