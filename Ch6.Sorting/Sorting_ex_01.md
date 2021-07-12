# Ex 01) 위에서 아래로 문제
### T 기업 코딩테스트 기출
- 하나의 수열을 큰수부터 작은 수의 순서로 정렬하는 프로그램을 만드시오.
***
- 입력조건
  - 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다.(1 <= N <= 500)
  - 둘째 줄부터 N+1 번째 줄까지 N개의 수가 입력된다. 수의 범위는 1 이상 100000이하의 자연수 이다.
- 출력조건
  - 입력으로 주어진 수열이 내맃마순으로 정렬된 결과를 공백으로 구분하여 출력한다. 동일한 수의 순서는 자유롭게 출력해도 괜찮다.
***
- 내가 푼 답안
```python
n = int(input())
array = []
for i in range(n):
    array[i] = int(input())
array=sorted(array, reverse=True)
print(array)
```
***
- 답안예시
```python
# N 입력받기
n = int(input())
# N개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))
# 파이썬 기본정렬 라이브러리를 이용하여 정렬 수행
array=sorted(array, reverse=True)
print(array)
```
***
💡 ```array.append``` 를 입력시에 이용해야 한다는 것을 기억하자.