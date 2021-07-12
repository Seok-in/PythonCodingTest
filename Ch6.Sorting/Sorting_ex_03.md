# Ex 03 ) 두 배열의 원소 교체
### 국제알고리즘대회 기출
- N개의 원소로 구성되어 있는 두 배열(A,B)이 있다.
- 배열의 원소는 모두 자연수이며 K 번의 바꿔치기를 할 수 있는데 이 때 배열 A의 원소들의 합이 최대가 되도록 하는 프로그램을 만드시오.
***
- 입력조건
  - 첫 번째 줄에 N, K 가 공백으로 구분되어 입력된다.(1 <= N <= 100000, 0 <= K <= N>)
  - 두 번째 줄에 배열 A의 원소들이 공백으로 구분되어 입력된다.
  - 세 번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력된다.
- 출력조건
  - 최대 K번의 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하시오.
***
- 내가 쓴 답안
```python
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = sorted(a)
b = sorted(b, reverse=True)

for i in range(k):
    if a[i] >= b[i]:
        break
    else:
        a[i], b[i] = b[i], a[i]

result = 0
for i in range(len(a)) :
    result += a[i]
print(result)
```
***
- 답안 예시
```python
# N과 K를 입력받기
n, k = map(int, input().split())
# 배열 A의 원소를 모두 입력받기
a = list(map(int, input().split()))
# 배열 B의 원소를 모두 입력받기
b = list(map(int, input().split()))
# 배열 A 오름차순
a = sorted(a)
# 배열 B 내림차순
b = sorted(b, reverse=True)

# 첫번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K 번 비교
for i in range(k):
    # A 의 원소가 B보다 작은경우
    if a[i] < b[i]:
        # 두 원소 교체
        a[i], b[i] = b[i], a[i]
    # A의 원소가 B의 원소보다 크거나 같을 때 반복문 탈출
    else :
        break
# 배열 A 원소의 합 출력
print(sum(a))
```
💡 배열의 입력방법과 sum과 같은 리스트의 알고리즘을 기억하도록 하자
💡 sorted의 사용법 또한 기억하자