import math


# 최소공배수 구하기
# 최소공배수 = (x*y) / gcd(x,y)
def factorization(x):
    d = 2
    res = []
    while d <= x:
        if x % d == 0:
            res.append(d)
            x = x / d
        else:
            d = d + 1
    return res


print(factorization(64))


# 소수 찾기
# 에라토스테네스의 체
# 일단 수를 다 쓴 다음 소수의 배수를 모두 지운다
def elatostenes(n):
    answer = 0
    chae = [False, False] + [True] * (n - 1)
    prime = []
    for i in range(2, n + 1):
        if chae[i] == True:
            prime.append(i)
            for j in range(2 * i, n + 1, i):
                chae[j] = False
    answer = len(prime)
    return answer


print(elatostenes(100))



def is_prime_number(n):
    """소수판별 함수"""
    if n == 0 or n == 1:  # 0,1 은 소수가 아님
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):  # sqrt(n)까지만 for문을 돌면서 확인하면 된다.
            if n % i == 0:  # 2~sqrt(num)까지 나누어 떨어지는 숫자가 있으면 소수가 아님
                return False

        return True
