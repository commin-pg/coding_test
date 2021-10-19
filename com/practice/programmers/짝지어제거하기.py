def solution(s):
    stack = []
    for ss in s:
        if len(stack) == 0:
            stack.append(ss)
        elif stack[-1] == ss:
            stack.pop()
        else:
            stack.append(ss)

    if len(stack) == 0:
        return 1
    else:return 0



s = ["eaaebbdccd", "cdc"]
for i in s:
    print(solution(i))
