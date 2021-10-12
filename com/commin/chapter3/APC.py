"""
입력
첫 줄에 문제의 개수 N, 현정이의 역량 L, 현정이가 대회중에 풀 수 있는 문제의 최대 개수 K가 주어진다.

둘째 줄부터 N개의 줄에 걸쳐 1 ~ N번째 문제의 쉬운 버전의 난이도 sub1, 어려운 버전의 난이도 sub2 가 순서대로 주어진다.

출력
현정이가 APC에 참가했다면 얻었을 점수의 최대값을 출력한다.

제한
1 ≤ N ≤ 100
1 ≤ L ≤ 50
1 ≤ sub1 ≤ sub2 ≤ 50
서브태스크 1 (100점)
K = N
서브태스크 2 (40점)
0 ≤ K ≤ N
"""

N, L, K = map(int, input().split())

easy, hard = 0, 0
for i in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1
# print(easy, hard)

ans = min(hard, K) * 140

if hard < K:
    ans += min(K - hard, easy) * 100

print(ans)
