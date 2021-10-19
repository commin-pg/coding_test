import math


# 첫째 행렬의 열 갯수 = 둘째 행렬의 행 갯수
def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]

    for row in range(len(answer)):
        for col in range(len(answer[row])):
            for k in range(len(arr1[0])):
                answer[row][col] += arr1[row][k] * arr2[k][col]
    return answer


# arr1 = [[1, 4], [3, 2], [4, 1]]  # 3 X 2 행렬
# arr2 = [[3, 3], [3, 3]]  # 2 X 2 행렬
arr1 = [[3, 1, 4]]
arr2 = [[3, 1, 1]]

print(solution(arr1, arr2))
