# 21:24 start 21:31 en

def beautifulDays(i, j, k):
    ret = 0
    A = list(map(str, [i for i in range(i, j + 1)]))
    for a in A:
        if abs(int(a) - int(a[::-1])) % k == 0:
            ret += 1
    return ret


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)
    print(result)
