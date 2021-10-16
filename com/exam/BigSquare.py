"""
가장 큰 정사각형
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	27063	8098	5789	29.231%
문제
n×m의 0, 1로 된 배열이 있다. 이 배열에서 1로 된 가장 큰 정사각형의 크기를 구하는 프로그램을 작성하시오.

0	1	0	0
0	1	1	1
1	1	1	0
0	0	1	0
위와 같은 예제에서는 가운데의 2×2 배열이 가장 큰 정사각형이다.

입력
첫째 줄에 n, m(1 ≤ n, m ≤ 1,000)이 주어진다. 다음 n개의 줄에는 m개의 숫자로 배열이 주어진다.

출력
첫째 줄에 가장 큰 정사각형의 넓이를 출력한다.

"""

N, M = map(int, input().split())
A = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
# DP[i][j] = i,j 까지 왔을 때, 가장 큰 정사각형의 한변의 길이
DP = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(N):
    for idx, v in enumerate(list(map(int, list(input())))):
        A[i + 1][idx + 1] = v

# mx = 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if A[i][j]:
            DP[i][j] = min(DP[i - 1][j], DP[i - 1][j - 1], DP[i][j - 1]) + 1
            # mx = max(DP[i][j], mx)
# print(mx ** 2)
print(max([max(i) for i in DP]) ** 2)
