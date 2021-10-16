def separateNumbers(s):
    if s[:1] == '0':
        print("NO")
        return
    else:
        # 1234
        idx = 1
        old_idx = 0
        old_old_idx = 0
        isOk = (False, '')
        cnt = 0
        while True:
            ss = s[old_idx:idx]
            sss = str(int(ss) + 1)
            if sss == s[idx:idx + len(sss)]:
                cnt += 1
                old_old_idx = old_idx
                old_idx = idx
                idx = idx + len(sss)
                if cnt == 1:
                    isOk = (True, ss)
            else:
                if isOk[0] and idx < len(s):
                    cnt = 0
                    old_idx = old_old_idx
                else:
                    idx += 1
                isOk = (False, '')

            if idx >= len(s):
                break
        if isOk[0]:
            print("YES {}".format(isOk[1]))
        else:
            print("NO")


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        separateNumbers(s)
