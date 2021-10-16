"""

가장 큰 증가 부분 수열
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	28732	13010	10313	45.118%
문제
수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 합이 가장 큰 증가 부분 수열의 합을 출력한다.

"""
import copy


def process(N):
    seq = list(map(int, input().split()))
    # print(seq)
    # DP[i] : i 까지 왔을때 합의 최대
    DP = copy.deepcopy(seq)
    mx = 0
    idx = 0
    for i in range(1, N):
        for j in range(i):
            if seq[i] > seq[j]:
                DP[i] = max(seq[i] + DP[j], DP[i])

        if max(DP) > mx:
            idx = i
            mx = max(DP)

    # print(idx, mx, seq[:idx + 1])
    ways = set([i for i in seq[:idx + 1] if i < seq[idx]])
    ways = list(ways) + [seq[idx]]
    print(ways)
    print(max(DP))


if __name__ == '__main__':
    N = int(input())
    process(N)
