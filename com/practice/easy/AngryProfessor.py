# 21:15 start 21:23 end

def angryProfessor(k, a):
    ret = len([i for i in a if i <= 0])  # 수업시간까지 도착한 학생들의 수
    if ret >= k:  # 수업시간까지 도착한 학생수가 임계치보다 더 많거나 같으면
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = angryProfessor(k, a)
    print(result)