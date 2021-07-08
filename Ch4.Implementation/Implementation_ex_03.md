# Ex 3) 왕실의 나이트 문제
- 행복 왕국의 왕실 전원은 체스판과 같은 8 X 8 좌표 평면이다
- 나이트는 특정한 위치에서 2가지 경우로 이동할 수 있다.
  - 수평으로 두 칸 이동한 후 수직으로 한 칸 이동
  - 수직으로 두 칸 이동한 후 수평으로 한 칸 이동
- 이 때 나이트의 위치가 주어졌을 때 이동할 수 있는 경우의 수를 구하시오.
- 단, 나이트는 왕실인 8 X 8 좌표 평면을 벗어날 수 없다.
***
- 입력조건
  - 첫째 줄에 8 X 8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다.
- 출력조건
  - 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.
***
- 내가 푼 답안
```python
x = input()
count = 0
row = int(x[1])
columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
movements = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
for i in range(len(columns)) :
    if x[0] == columns[i] :
        column = i+1
for movement in movements :
    row += movement[0]
    column += movement[1]
    if row >= 1 and column >= 1 and row <= 8 and column <= 8 :
        count += 1
    row -= movement[0]
    column -= movement[1]
print(count)
```
- 답안 예시
```python
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]))-int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]

    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
        result += 1
print(result)
```
***
- 내가 푼 답안에서는 ord 라는 문법을 몰라 for문을 한번 더 사용하여 column의 값을 구할 수 밖에 없었다.
💡 답안 예시 처럼 ord 함수(문자를 숫자로 반환하기) 활용도 알아두면 좋을 거 같다.<br>
💡 또한 이번에 튜플을 원소로 받는 리스트를 구성하였을 때의 활용도 익숙하지가 않아 단번에 떠올리기 어려웠다.<br>
💡 문자열도 배열이기에 각각의 글자를 string[n]으로 가져올 수 있다는 것을 알아두자.<br>
***
#### 문제해설
- 앞서 다룬 상하좌우 문제와 유사하나 풀이법은 다르게 풀이하였다.
- dx, dy 리스트를 선언해서 이동할 방향을 기록할 수 있는 방법도 있으나 steps를 활용하여 dx dy의 변수 기능을 대신하는 방법도 있다는 것을 참고하도록 하자.