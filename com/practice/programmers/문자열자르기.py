def process(s, cutting):
    ss = []
    idx = 0
    cut = cutting
    while True:
        if cut > len(s):
            if s[idx:len(s)] != '':
                ss = ss + [s[idx:len(s)]]
            break
        ss = ss + [s[idx:cut]]
        idx = cut
        cut += cutting

    tmp_str = ''
    result = ''
    cnt = 0
    for idx, slice_str in enumerate(ss):
        if cnt == 0:
            tmp_str = slice_str
            cnt += 1
        else:
            if slice_str == tmp_str:
                cnt += 1
                if idx == len(ss) - 1:
                    result += str(cnt) + tmp_str
            else:
                if cnt > 1:
                    result += str(cnt) + tmp_str
                else:
                    result += tmp_str
                tmp_str = slice_str
                cnt = 1
                if idx == len(ss) - 1:
                    result += tmp_str
    return len(result)

if __name__ == '__main__':

    s = input()
    if len(s) == 1:
        print(1)
    else:
        ret = 10000000000000
        for i in range(1, len(s) // 2 + 1):
            ret = min(process(s, i), ret)

        print(ret)

# def dfs(s,n):
#     if
