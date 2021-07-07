# Ex 3) 숫자 카드 게임
#### 2019 국가 교육기관 코딩테스트 기출
- 숫자가 쓰인 카드들이 N X M 형태로 놓여있다. (N은 행, M은 열)
- 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택하고 그 행에서 가장 낮은 숫자를 선택한다.
- 이후 다음 행에서도 가장 숫자가 낮은 카드를 뽑게 되는데 후에 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야한다.
***
- 입력조건
  - 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로하여 각각 자연수로 주어진다. ( N, M <= 100)
  - 둘째 줄 부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 숫자는 1 이상 10000이하 이다.
- 출력조건
  - 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.
***
- 내가 푼 답안
```python
n, m = map(int, input().split())
result = 0;
for i in range(n):
    data = list(map(int, input().split()))
    min_data = min(data)
    if result < min_data :
        result = min_data

print(result)
***
```
- 답안 예시 1
```python
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value + min(data)
    #가장 작은 수 들 중에서 가장 큰 수 찾기
    result = max(result,min_value)
print(result)
```
***
- 답안 예시 2
  - 2중 반복문 구조를 이용
```python
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = 10001
    for a in data:
            min_value = min(min_value, a)
    #가장 작은 수 들 중에서 가장 큰 수 찾기
    result = max(result,min_value)
print(result)
```
***
- min함수 사용 뿐만아니라 max를 이용해서도 큰 값을 찾을 수 있도록 적용해봐야겠다.
- 2중 반복문을 사용하는 경우도 있다는 것을 염두해야 겠다.