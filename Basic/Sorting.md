# Sorting (정렬)
- 정렬이란 데이트를 특정한 기준으로 순서대로 나열하는 것을 말한다.
- 추후 이진탐색을 사용할 때 전처리 과정이니 잘 알아두어야 한다.
***
- Selection Sort(선택정렬)
  - 선택정렬은 가장 작은 데이터를 선택해 맨 앞에 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 의미한다.
  - 시간복잡도는 O(N^2)
 ```python
  array = [7,2,1,3,4,5,6,9,8,0]
  
  for i in range(len(array)) :
      min_index = i
      for j in range(i+1,len(array)) :
          if array[min_index] < array[j] :
              # 파이썬에서만 가능한 스왑
              array[min_index], array[j] = array[j], array[min_index]
    
  print (array)
  ```
  ***
- Insertion Sort(삽입정렬)
  - 특정한 데이터를 적절한 위치에 삽입한다는 의미
  - 정렬되어 있는 데이터 리스트에서 적절한 위치를 찾은 뒤에 그 위체에 삽입된다.
   - 삽입 정렬은 첫 번째 데이터는 그 자체로 정렬되어 있다고 판단하고 두 번째 데이터부터 시작한다.
   - 시간복잡도는 O(N^2)이나 데이터가 거의 정렬되어 있는상태면 O(N)의 시간복잡도를 가진다.
  ```python
  array = [7,5,9,0,3,1,6,2,4,8]
  for i in range(1, len(array)):
      # 인덱스 i 부터 1까지 감소하며 반복하는 문법
      for j in range(i,0,-1):
          if array[j] < array[j-1] :
              array[j], array[j-1] = array[j-1], array[j]
          # 자기보다 작은 데이터를 만날 시에 멈춤
          else :
              break
  ```
***
- Quick Sort(퀵 정렬)
  - 정렬 중에 가장 많이 사용되는 알고리즘이다.
  - 피벗(pivot)이 사용되며 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 '기준'을 바로 피벗이라고 표현한다.
  - 리스트에서 첫 데이터를 피벗으로 정하고 왼쪽에서부터 피벗보다 큰 데이터를 찾고 오른쪽에서부터 피벗보다 작은 데이터를 찾는다.
  - 그 다음 큰 데이터와 작은 데이터의 위치를 서로 교환해준다.
  - 이러한 과정을 반복하면 피벗에 대해 정렬이 수행된다.
  - 그 후 서로 엇갈린다면 피벗과 작은데이터의 위치를 변경하여 분할시켜서 한다.
  - 퀵 정렬의 시간복잡도는 O(NlogN) 이다. 다른 정렬에 비해 빠른 편이다.
```python
array = [5,7,9,0,3,1,6,2,4,8]
def quick_sort(array,start,end):
  if start >= end :
    return
  pivot = start
  left = start + 1
  right = end
  while left <= right :
    # 피벗보다 큰 데이터를 찾을 때 까지 반복
    while left <= end and array[left] <= array[pivot]:
      left += 1
    # 피벗보다 작은 데이터를 찾을 때 까지 반복
    while right > start and array[right] >= array[pivot]:
      right -= 1
    # 엇갈렸다면 작은 데이터와 피벗을 교체
    if left > right :
      array[right], array[pivot] = array[pivot], array[right]
    # 엇갈리지 않았다면 작은 데이터와 큰데이터를 교체
    else:
      array[left], array[right] = array[left], array[right]

  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
  quick_sort(array,start,right-1)
  quick_sort(array,right+1,end)
quick_sort(array, 0 ,len(array)-1)
print(array)
```
- 위 문법은 널리 사용되고 있는 직관적인 형태의 퀵정렬이다.
```python
array = [5,7,9,0,3,1,6,2,4,8]
def quick_sort(array):
  # 리스트가 하나 이하의 원소만을 담고 있다면 종료
  if len(array) <= 1:
    return array
  # 피벗은 첫번째 원소
  pivot = array[0]
  # tail은 피벗을 제외한 리스트
  tail = [1:]

  # 왼쪽분할
  left_side = [x for x in tail if x <= pivot]
  # 오른쪽분할
  right_side = [x for x in tail if x > pivot]

  # 분할 이후 왼쪽 부분과 오른쪽부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
  return quick_sort(left_side) +[pivot]+quick_sort(right_side)

print(quick_sort(array))
```
- 파이썬의 장점을 살려 간결하게 만든 퀵 정렬 소스코드이다.
***
- Count Sort (계수 정렬)
  - 계수정렬은 특정한 조건이 부합할때만 사용할 수 있으며 매우 빠른 정렬 알고리즘이다.
  - 데이터의 개수가 N 최댓값이 K 일때 최악의 경우에도 O(N+K)를 보장한다.
  - 원리 또한 매우 간단하며 데이터의 크기 범위가 제한되어 정수형태로 표현할 수 있을때만 사용할 수 있다(Ex. 성적 데이터)
```python
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 범위를 포함하는 리스트 선언
count = [0] * (max(array)+1)

for i in range(len(array)):
  count[array[i]] += 1
for i in range(len(count)):
  for j in range(count[i]) :
    print( i, end = ' ')
```
***
- 파이썬의 정렬 라이브러리
  - 파이썬은 기본 정렬 라이브러리인 sorted()를 제공한다.
  - 리스트에서도 array.sort()를 이용하여 정렬할 수 있다.
  - 정렬 라이브러리는 시간복잡도가 O(NlogN)이다.