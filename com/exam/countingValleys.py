"""

"""


def countingValleys(steps, path):
    state = 0
    v = 0
    for i in path:
        state += i
        if state == 0 and i == 1:
            v += 1
    return v


if __name__ == '__main__':
    steps = int(input().strip())
    path = list(map(int, ('UD'.index(i) * -2 + 1 for i in list(input()))))
    result = countingValleys(steps, path)
    print(result)
