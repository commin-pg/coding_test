# 23:27 start

def maxMin(k, arr):
    arr_set = set(arr)
    mn = 5000000
    for i in arr_set:
        if arr.count(i) == k:
            return 0
    arr = sorted(arr)
    old = 0
    for idx in range(k, len(arr) + 1):
        # print(arr[old:idx], max(arr[old:idx]), min(arr[old:idx]))
        if max(arr[old:idx]) - min(arr[old:idx]) < mn:
            mn = max(arr[old:idx]) - min(arr[old:idx])
        old += 1

    return mn


if __name__ == '__main__':
    n = int(input().strip())
    k = int(input().strip())

    arr = []

    # for _ in range(n):
    #     arr_item = int(input().strip())
    #     arr.append(arr_item)
    arr = sorted(int(input()) for _ in range(n))
    print(min(arr[i + k - 1] - arr[i] for i in range(0, n - k - 1)))

    # result = maxMin(k, arr)
    # print(result)
