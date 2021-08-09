n = int(input())
array=[]
for i in range(n):
    array.append(list(input().split()))

array = sorted(array, key=lambda student:student[1])

for student in array:
    print(student[0], end=' ')