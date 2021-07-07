# Ex 4) 1이 될때까지
#### 2018년 E 기업 알고리즘 대회
- 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
  - N에서 1을 뺀다.
  - N을 K로 나눈다.
- 이 때 N이 1이 될 때 까지 과정을 수행해야하는 최소 횟수를 구하시오.
***
- 입력조건
  - 첫째 줄에 N과 K가 공백으로 구분되며 각각 자연수로 주어진다. 이때 N 은 항상 K 보다 크거나 같다.
    - (2 <= N <= 100000), (2 <= K <= 100000)
- 출력조건
  - 첫째 줄에 N이 1이 될때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.
***
- 내가 푼 답안
```python
n, k = map(int, input().split())
count = 0

while n != 1:
    if n%k == 0 :
        n /= k
    else :
        n -= 1
    count += 1
print(count)
```
***
- 답안 예시 1
```python
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k :
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k  != 0 :
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1
# 마지막 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1
print(result)
```
***
- 답안 예시 2
  - N이 100억이상의 큰수가 되는 경우에도 빠르게 동작하려면, N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식으로 소스코드를 작성할 수 있다.
```python
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while True:
    #(N==K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n//k) * k
    result += (n-target)
    n =target
    # N이 K보다 작을 때 반복문 탈출
    if n < k :
        break
    # K로 나누기
    result += 1
    n //= k
# 마지막 남은 수에 대하여 1 씩 빼기
result += (n-1)
print(result)
```