# Binary Search(이진탐색)
- 순차탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례로 확인하는 방법
```python
# 순차 탐색 소스코드 구현
def sequential_search(n,target,array):
    # 각 원소를 하나씩 확인하며
    for i in range(n) :
        # 현재 원소가 찾는 원소와 동일하면
        if array[i] == target:
            # 현재의 위치 반환
            return i + 1
print("생성할 원소 개수를 입력하세요:")
input_data = input().split()
n=int(input_data[0]) # 원소 개수
target = input_data[1] # 찾고자하는 문자열

print("문자열을 입력하세요  :")
array = input().split()

# 순차탐색 수행 결과 출력
print(sequential_search(n, target, array))
```
- 순차탐색은 데이터 정렬 여부와 상관없이 앞에 있는 원소부터 하나씩 차례로 확인해야 하므로 시간 복잡도는 O(N)이다.
***
- 이진탐색 : 시작점, 끝점, 중간점을 이용하며, 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 과정이다.
```python
# 재귀함수로 이진 탐색 소스코드 구현
def binary_search(array, target, start, end):
    if start > end :
        return None
    mid = (start + end) // 2
    # 찾은경우 중간점 인덱스 반환
    if array[mid] == target :
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target :
        return binary_search(array, target, start, mid -1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else : 
        return binary_search(array, target, mid+1, end)
```
```python
# 반복문으로 구현
def binary_search(array, target, start, end):
    while start <= end :
        mid = (start+end)//2
        if array[mid] == target :
            return mid
        elif array[mid] > target :
            end = mid -1
        else :
            start = mid + 1
    return None
```