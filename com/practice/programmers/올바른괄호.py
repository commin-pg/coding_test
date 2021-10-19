def solution(s):
    stack = list(s)
    tmp = []
    while len(stack) > 0:
        if not tmp:
            tmp.append(stack.pop())
            continue
        else:
            ss = stack.pop()
            if (ss == "(" and tmp[0] == ")"):
                tmp.pop()
                continue
            else:
                tmp.append(ss)
    # print(stack, tmp)
    if len(tmp) == 0:
        return True
    else:
        return False


arr = ["()()", "(())()", ")()("]
for a in arr:
    print(solution(a))
