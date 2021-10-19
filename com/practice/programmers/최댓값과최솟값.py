def solution(s):
    lst = list(map(int, s.split()))
    return "{} {}".format(min(lst), max(lst))


s = ["1 2 3 4", "-1 -2 -3 -4", "-1 -1"]
for ss in s:
    print(solution(ss))
