# 백준 10989
#
# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

import sys
input = sys.stdin.readline

# 입력
N = int(input())

# counting sort, 근데 ^ㅣㅂ 왜 기수정렬에서 계수정렬을 쓰라 하지..?
# N은 10000이하의 수니까 counting sort로 index에 해당 값을 counting하기 위해
count = [0] * 10001

for i in range(N):
    count[int(input())] += 1

for i in range(10001):
    if count != 0:
        # count[i]의 값만큼 i 출력
        for _ in range(count[i]):
            print(i)


