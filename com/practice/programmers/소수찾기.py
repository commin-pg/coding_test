from itertools import permutations # 조합
import math

def is_prime_number(n):
    """소수판별 함수"""
    if n == 0 or n == 1:  # 0,1 은 소수가 아님
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):  # sqrt(n)까지만 for문을 돌면서 확인하면 된다.
            if n % i == 0:  # 2~sqrt(num)까지 나누어 떨어지는 숫자가 있으면 소수가 아님
                return False
        return True


def solution(numbers):
    answer = []
    for i in range(1,len(numbers)+1):
        arr = list(permutations(numbers, i))
        for j in range(len(arr)):
            num = int(''.join(map(str,arr[j])))
            if is_prime_number(num):
                answer.append(num)

    return len(set(answer))


s = ["17", "011"]
for ss in s:
    print(solution(ss))
