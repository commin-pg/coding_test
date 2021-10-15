import math
import os
import random
import re
import sys


def equalizeArray(arr):
    arr_set = set(arr)
    ret = 0
    mx = 0
    num = 0
    for v in arr_set:
        old_mx = mx
        mx = max(mx, arr.count(v))
        if old_mx != mx:
            num = v
    arr_set.remove(num)
    for v in arr_set:
        ret += arr.count(v)
    return ret


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = equalizeArray(arr)
    print(result)
