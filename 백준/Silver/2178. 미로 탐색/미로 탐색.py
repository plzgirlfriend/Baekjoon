# 백준 2178

# N×M크기의 배열로 표현되는 미로가 있다.
#
# 1	0	1	1	1	1
# 1	0	1	0	1	0
# 1	0	1	0	1	1
# 1	1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
#
# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
#
# 입력
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.
#
# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

from collections import deque

# 좌우
x = [0, 1, 0, -1]
# 상하
y = [1, 0, -1, 0]

# 입력
N, M = map(int, input().split())

# N*M 배열(0)
A = [[0]*M for _ in range(N)]

# N*M 배열(False)
visited = [[False]*M for _ in range(N)]

# A에 데이터 저장
for i in range(N):
    num = list(input())
    for j in range(M):
        A[i][j] = int(num[j])

def bfs(n,m):
    queue = deque()

    queue.append((n,m))
    visited[n][m] = True

    # queue에 비어있지 않을 때
    while queue:
        now = queue.popleft()

        # 상하좌우 탐색
        for i in range(4):
            xx = now[0] + x[i]
            yy = now[1] + y[i]

            # 좌표가 list 범위 안에 있는지 확인해야함
            # 좌표가 0인지 1인지 검사해야함
            if xx >= 0 and yy >= 0 and xx < N and yy < M:
                if A[xx][yy] != 0 and not visited[xx][yy]:
                    visited[xx][yy] = True
                    # 그 값에 + 1
                    A[xx][yy] = A[now[0]][now[1]] + 1
                    queue.append((xx, yy))

bfs(0,0)

print(A[N-1][M-1])


