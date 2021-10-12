# T = input()
# N = int(input())
# C = list(map(int, input().split()))
# print(C)

def check(N, candys):
    for i in range(N):
        if candys[i] % 2 == 1:
            candys[i] += 1
    return len(set(candys)) == 1


def teacher(N, candys):
    tmp_list = [0 for i in range(N)]
    for idx in range(N):
        if candys[idx] % 2:
            candys[idx] += 1
        candys[idx] //= 2
        tmp_list[(idx + 1) % N] = candys[idx]

    for idx in range(N):
        candys[idx] += tmp_list[idx]
    return candys


def process():
    N, candys = int(input()), list(map(int, input().split()))
    cnt = 0
    while not check(N, candys):
        cnt = cnt + 1
        candys = teacher(N, candys)
    print(cnt)


for i in range(int(input())):
    process()
