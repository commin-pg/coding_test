"""
메모이제이션 : 다음 상태를 저장하고, 사용하기

푸는 순서
1. 상태를 정의한다.
2. 점화식을 찾는다(구한다)
3. 시간복잡도를 계산한다.
4. 코딩한다.

1. Top-Down (재귀)
2. Bottom-Up (반복문)

"""

"""
누적합

import copy

A = [i for i in range(10)]
print(A)
DP = copy.deepcopy(A)
for i in range(1, 10):
    DP[i] = DP[i - 1] + DP[i]
print(DP)
# i = 3 j = 2
print(DP[3] - DP[2 - 1] == A[3] + A[2])

# DP[i] = i까지의 합
# i 부터 j 까지의 합은 DP[i] - DP[j-1]

"""
