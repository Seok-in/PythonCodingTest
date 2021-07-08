# Ex 1) 거스름돈 문제
- 손님에게 거슬러줘야 할 동전의 최소 개수는 ?
- 단 거슬러줘야할 돈 N은 항상 10의 배수이며 카운터에는 500, 100, 50, 10 원짜리 동전이 무한히 존재한다.

***
- 내가 푼 답안
```python
n = int(input())
count = 0
coin_type=[500,100,50,10]
for i in coin_type :
    count = count + n//i
    n = n%i

print(count)
```
***
- 답안 예시
```python
# n 입력받기
n = int(input()) 
count = 0

# 큰 단위의 화폐부터 차례로 확인
coin_type=[500,100,50,10]
for i in coin_type :
    count += n//i  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= i

print(count)
```
***
- ```count = count + n//i``` 대신 ```count += n//i```를 사용하면서 변수호출을 한번 더 안해도 되는 간편함이 있다. 추후 등호 대신 +=, %= 등을 이용하여야겠다.