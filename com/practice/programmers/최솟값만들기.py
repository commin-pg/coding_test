def solution(A, B):
    answer = [a * b for a, b in zip(sorted(A), sorted(B, reverse=True))]
    return sum(answer)


# A, B = [1, 4, 2], [5, 4, 4]
A, B = [1, 2], [3, 4]
print(solution(A, B))
