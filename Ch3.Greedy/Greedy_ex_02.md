# Ex 2) 큰 수의 법칙
#### 2019년 국가 교육기관 코딩테스트 기출
- 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
- 이 때 배열의 특정한 인덱스는 연속해서 K번을 초과하여 더해질 수 없다.
- 이 때 가장 큰 수를 만드는 법은?
***
- 입력 조건
  - 첫째 줄에 N, M, K의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
    - (2 <= N <= 1000),(1 <= M <= 10000), (1 <= K <= 10000)
  - 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 각각의 자연수는 10000이하의 숫자로 주어진다.
  - 입력으로 주어지는 K는 항상 M보다 작거나 같다.
  
- 출력 조건
  - 정해진 큰 수의 법칙에 따라 더해진 답을 출력한다.
***
- 내가 푼 답안
  ```python
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    result = 0
    count = 0
    while True :
        result += data[0]
        count += 1
        if count%k == 0 :
            result += data[1]
            count += 1
        if count == m :
            break;
       
    print(result)
    ```
***
- 답안 예시 1
    ```python
    # N, M, K 를 공백으로 구분하여 입력받기
    n, m, k = map(int, input().split())
    # N개의 수를 공백으로 구분하여 입력받기
    data = list(map(int, input().split()))
    
    data.sort() # 입력받은 수 정렬
    first = data[n-1] # 가장 큰 수
    second = data[n-2] # 2번째로 큰 수

    result = 0

    while True :
        for i in range(k): # 가장 큰 수를 K번 더하기
            if m == 0 : # m = 0 이면 반복문 탈출
                break
            result += first
            m-=1 # 더할 때 마다 1 씩 빼기
        if m == 0 : # m = 0 이면 반복문 탈출
            break
        result += second # 두번째로 큰 수 한번 더하기
        m-=1 # 더할 때 마다 1 씩 빼기
    print(result)
***
- 답안 예시 2
    - 위 답안인 경우 M이 작을경우 상관 없지만 M의 크기가 100억 이상이면 시간초과 판정을 받을 수 있다.
    - 따라서 수학적 아이디어인 반복되는 수열의 특성을 확인하여 문제해결을 해야한다.
    - 가장 큰 수가 더해지는 횟수는 ```int(M / (K+1) * K + M % (K+1))``` 인 것을 이용한다.

    ```python
   # N, M, K 를 공백으로 구분하여 입력받기
    n, m, k = map(int, input().split())
    # N개의 수를 공백으로 구분하여 입력받기
    data = list(map(int, input().split()))
    
    data.sort() # 입력받은 수 정렬
    first = data[n-1] # 가장 큰 수
    second = data[n-2] # 2번째로 큰 수

    # 가장 큰 수가 더해지는 횟수 계산
    count = int(m/(k+1)) * k
    count += m % (k + 1)

    result = 0
    result += (count) * first # 가장 큰 수 더하기
    result += (m-count) * second # 2번째로 큰 수 더하기

    print(result)
    ```