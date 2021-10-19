"""
1. 왼쪽에서 0자 이상의 문자를 제거
2. s 의 오른쪽에서 0자이상의 문자 제거
3. s 의 왼쪽에서 0자이상의 문자를 제거하고, 오른쪽에서 0자이상의 문자를 제거

abcde
1. abcde
2. abcd
3. bcde
4. bcd
"""

# global count
# global res
# res = set()
# count = 0
#
#
# def reduce(string):
#     global count, res
#     if not string:
#         return
#     if string not in res:
#         res.add(string)
#         count += 1
#     else:
#         return
#
#     reduce(string[:-1])
#     reduce(string[1:])
#     if len(string) >= 2:
#         reduce(string[1:-1])
#
#
# reduce("abcde")
# print(count)
# print(res)

cnt = 0


# def dfs(s, ret):
#     global cnt
#     if not s or s in ret:
#         return
#
#     if s not in ret:
#         cnt += 1
#         ret.add(s)
#     dfs(s[:-1], ret)
#     dfs(s[1:], ret)
#     if len(s)>=2:
#         dfs(s[1:-1])
#
# def subsringCalculator(s):
#     ret = set()
#     dfs(s, ret)
#
#
#
#
# if __name__ == '__main__':
#     subsringCalculator(input())
#     print(cnt)


# Python3 program to print all possible
# substrings of a given string

#kincenvizh


# Function to print all sub strings
cnt = 0


def subString(Str, n):
    global cnt
    lst = set()
    for lf in range(1, n + 1):
        for rf in range(n - lf + 1):
            idx = rf + lf - 1
            sss = ''

            for k in range(rf, idx + 1):
                sss += Str[k]
            lst.add(sss)
            cnt += 1
    print(cnt)
    print(len(lst))

Str = input()
subString(Str, len(Str))