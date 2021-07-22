n, m = map(int, input().split())
result = 0
array=[]
for i in range(n):
  array = list(map(int, input().split()))
  result = max(result, min(array))


print(result)

# 2차원 배열로 굳이 입력을 받아야 할 필요가 없다는 것을 인지하자.