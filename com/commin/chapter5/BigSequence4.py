"""
가장 긴 증가하는 부분 수열 4 스페셜 저지
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	16727	6479	4910	39.349%
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.

"""
import copy


def process(N):
    SEQ = list(map(int, input().split()))
    DP = copy.deepcopy(SEQ)
    mx = 0
    idx = 0
    for i in range(1, N):
        for j in range(i):
            if SEQ[i] > SEQ[j]:
                DP[i] = max(SEQ[i] + DP[j], DP[i])
        if max(DP) > mx:
            idx = i
            mx = max(DP)

    # print(idx, mx, SEQ[:idx + 1])
    ways = set([i for i in SEQ[:idx + 1] if i < SEQ[idx]])
    ways = list(ways) + [SEQ[idx]]
    ways_str = list(map(str, ways))

    print(len(ways))
    print(' '.join(ways_str))

if __name__ == '__main__':
    N = int(input())
    process(N)
