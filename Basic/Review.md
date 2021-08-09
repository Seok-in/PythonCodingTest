# 꼭 기억해야할 것
- 공백을 기준으로 정수를 입력받는 것 : ```n,m,k = map(int, input().split())```
- 공백을 기준으로 하여 리스트로 정수를 입력받는 것 : ```data = list(map(int, input().split()))```
- 줄 바꿈으로 하나씩 리스트로 정수를 입력받는 것
```python
array = []
for i in range(n):
    array.append(int(input))
```
- 2차원 배열 초기화 : ```array = [[0] * m for _in range(n)]```
- 2차원 배열의 선언 : 
```python
n, m = map(int, input().split())
array = [[0] * m for _ in range(n)]
for i in range(n):
    array.append(list(map(int, input().split())))

```
***
- sorted vs sort
  - sorted : ```array = sorted(array, reverse=True)```
  - sort : ```array.sort(reverse=True)```