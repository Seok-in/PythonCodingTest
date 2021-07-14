# Ex 1 ) 부품 찾기 문제
- 가게에 N개의 부품이 있다. 이 때 손님은 M개의 부품을 구매하려고 한다.
- 이 때 손님이 요청하는 M 개의 부품에 대해 가게에 있는지 여부를 출력하시오.
***
- 입력조건
  - 첫째 줄에 정수 N이 주어진다. (1 <= N =< 1000000)
  - 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다.
  - 셋째 줄에는 정수 M이 주어진다. (1 <= M =< 100000)
  - 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다.
- 출력조건
  - 첫째 줄에 공백으로 구분하여 각 부품의 존재여부에 따라 yes no 를 출력한다.
***
- 내가 푼 답안
```python
n = int(input())
array_n= map(int,input().split())
m = int(input())
array_m= map(int,input().split())

array_n =sorted(array_n)

def binarySearch(array, target, start, end):
    if start > end:
        return False
    mid = (start+end) // 2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binarySearch(array, target, start, mid-1)
    else:
        return binarySearch(array, target, mid + 1, end)


for i in range(len(array_m)):

    if binarySearch(array_n, array_m[i], 0, n - 1):
        print("yes" + " ")
    else :
        print("no" + " ")
```
***
- 답안 예시
```python
# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end :
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스반환
        if array[mid] == target :
            return mid
        # 중간점의 값보다 찾고자하는 값이 적은 경우 왼쪽 확인
        elif array[mid] > target :
            end = mid -1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else :
            start = mid +1
    return None

# N, M, 정수들 입력
n = int(input())
array = list(map(int,input().split()))
# 이진 탐색 전 사전 정렬
array.sort()
m = int(input())
x = list() map(int,input().split())

# 부품번호를 하나씩 확인
for i in x:
    # 해당 부품 존재 여부 확인
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else :
        print('no', end = ' ')
```
***
- 답안 예시 2 (계수 정렬)
```python
# N 입력받기
n = int(input())
array = [0] * 1000001

# 가게에 있는 부품 전체를 입격받아서 기록
for i in input().split():
    array[int(i)] = 1
# M 입력받기
m = int(input())
# M개의 정수 입력받기
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    if array[i] == 1 :
        print('yes', end=' ')
    else :
        print('no', end = ' ')
```
***
- 답안예시3 (집합 자료형 이용)
```python
n = int(input())
# 전체 부품번호를 집합자료형에 기록
array = set(map(int,input().split()))

# M과 정수 입력받기
m = int(input())
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i  in x:
    if i in array :
        print('yes', end=' ')
    else:
        print('no', end=' ')
```
***
