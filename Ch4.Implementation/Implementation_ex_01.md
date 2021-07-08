# Ex 1) 상하좌우 문제
- 여행가 A는 N X N 정사각형 공간 위인 (1,1) 제일 왼쪽 제일 위에 서있다.
- 이때 여행 계획서에는 L, R, U, D 중 하나의 문자가 반복적으로 적혀 있다.
  - L(왼쪽으로 1칸), R(오른쪽으로 1칸), U(위로 1칸), D(아래로 1칸)
- A가 N X N 정사각형 공간을 벗어나는 움직임은 무시된다.
- 이때 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오
***
- 입력조건
  - 첫째 줄에 공간의 크기를 나타내는 N이 주어진다.
  - 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다.
- 출력조건
  - 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표(X,Y)를 공백으로 구분하여 출력한다.
***
- 내가 푼 답안
```python
n = int(input())
x, y = 1, 1
plans = input().split()
for i in plans:
    if i == 'L':
        y -= 1
        if y == 0 :
            y += 1
    elif i == 'R':
        y += 1
        if y > n:
            y -= 1
    elif i == 'U':
        x -= 1
        if x == 0 :
            x += 1
    elif i == 'D':
        x += 1
        if x > n :
            x -= 1
print(x,y)
```
***
- 답안 예시
```python
# N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans :
    # 이동 후 좌표 계산
    if plan == move_types[i]:
        nx = x + dx[i]
        ny = y + dy[i]

    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
```
***
💡 답안 예시처럼 이동 값을 따로 구분하여 좌표에 한번에 더해줘서 풀이할 수 있다는 것을 염두하자.