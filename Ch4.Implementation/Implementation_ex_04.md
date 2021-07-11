# Ex 4) 게임 개발 문제
- 게임 캐릭터가 맵 안에서 움직이는 시스템을 개발 중이다. 캐릭터가 있는 장소는 1 X 1 크기의 정사각형으로 이루어진 N X M 크기의 직사각형으로, 각각의 칸은 육지 또는 바다이다.
- 캐릭터는 동서남북 중 한 곳을 바라본다.
- 맵의 각 칸은 (A, B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다. 캐릭터는 상하좌우 움직일 수 있으며 바다로 되는 공간에는 갈 수 없다.
- 캐릭터의 이동 메뉴얼이다.
  - 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 90도 회전)부터 차례대로 갈 곳을 정한다.
  - 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다. 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
  - 만약 네 방향 모두 가본 칸이거나 바다로 되어 있는 경우 바라보는 방향을 유지한채 한칸 뒤로 가고 1단계로 돌아간다. 단, 이 때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
- 위 과정을 반복적으로 수행하면서 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.
***
- 입력조건
  - 첫째 줄에 맵의 크기 세로 N 과 가로 M 을 공백으로 구분하여 입력받는다.
  - 둘째 줄에 게임 캐릭터가 있는 좌표 (A, B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다. 방향 d는 다음과 같다.
    - 0 : 북쪽, 1 : 동쪽, 2 : 남쪽, 3 : 서쪽
  - 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽에서 동쪽 순서대로 주어지며 맵의 외곽은 항상 바다로 되어있다.
  - 처음 캐릭터의 위치는 항상 육지이다.
- 출력조건
  - 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다. 
***
- 답안 예시
```python

# N, M 을 공백으로 구분하여 입력받기
n,m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
# 2차원 배열
d = [[0]* m for _ in range(n)]
# 현재 캐릭터의 X, Y, 방향 입력받기
x, y, direction = map(int, input().split()
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n)
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1 :
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True :
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후에 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dx[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else :
            break
        turn_time = 0
# 정답 출력
print(count)

```
***
- 위 문제는 어려움을 많이 겪어 추후 다시 한번 풀어보도록 해야겠다.<br>
💡 함수를 이용하는 것을 생각하지 못하였음.<br>
💡 2차원 배열의 초기화 ```array = [[0]*m for _ in range(n)]```<br>
💡 2차원 배열 입력받기<br>
    ```python
    for i in range(n):
        array.append(list(map(int, input().split())))
    ```<br>
💡 turn_time  과 count 변수를 넣어서 활용할 생각을 못했음.<br>
💡 direction을 global 변수로 사용할 것도 유의할 것.<br>
***
#### 문제해설
- 전형적인 시뮬레이션 문제로 반복적인 숙달이 필요하다.
- 일반적으로 방향을 설정해서 이동하는 문제 유형에서는 dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적이다.