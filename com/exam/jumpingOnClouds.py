def jumpingOnClouds(c):
    C_ = []
    for v in c:
        C_ = C_ + [(v + 1) % 2]  # 0->1 , 1->0

    ret = 0
    idx = 0
    while True:
        if (idx + 1) >= len(C_):
            break
        if len(C_) - (idx + 1) == 1:
            ret += 1
            idx += 1
            break
        if sum(C_[idx:idx + 3]) == 3:
            idx += 2
            ret += 1
        elif sum(C_[idx:idx + 3]) == 2:
            if C_[idx + 1] == 0:
                idx += 2
            elif C_[idx + 2] == 0:
                idx += 1
            ret += 1
    return ret


if __name__ == '__main__':
    n = int(input())  # 배열 개수
    c = list(map(int, input().rstrip().split()))
    ret = jumpingOnClouds(c)
    print(ret)
