from itertools import permutations


def elatostenes(n):
    chae = [False, False] + [True] * (n - 1)
    prime = []
    for i in range(2, n + 1):
        if chae[i] == True:
            prime.append(list(str(i)))
            for j in range(2 * i, n + 1, i):
                chae[j] = False
    return prime


def solution(numbers):
    answer = 0
    for i in range(len(numbers)+1):
        print(list(permutations([0, 1, 1], i)))

    return answer


s = ["17", "011"]
for ss in s:
    print(solution(ss))
