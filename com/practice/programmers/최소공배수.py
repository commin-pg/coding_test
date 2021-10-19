import math
import copy

"""
1. 내림차순으로 arr 정렬
2. 앞에서부터 2개씩 , 즉 arr[i], arr[j] 의 최소공약수를 찾고, 그로부터 최소공배수를 계산하여 arr[i+1]에 넣음
3. arr의 맨 마지막 원소값이 전체 arr이 최소공배수

# 두 수의 최소공배수는 x*y//gcd(x,y)
"""


def solution(arr):
    answer = 0

    arr = sorted(arr, reverse=True)
    aa = copy.deepcopy(arr)
    for i in range(len(arr) - 1):
        gc = math.gcd(arr[i], arr[i + 1])
        arr[i + 1] = arr[i] * arr[i + 1] // gc
    print(aa)
    print(arr)
    answer = arr[-1]
    return answer


arr = [[2, 4, 6, 8], [1, 2, 3], [168, 180]]
for a in arr:
    print(solution(a))

# 다른사람 풀이
def nlcm(num):
    answer = num[0]
    for n in num:
        answer = n * answer // math.gcd(n, answer)
    return answer
