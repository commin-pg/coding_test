# def weightedUniformStrings(str, queries):
#     ret = []
#     old = ''
#     for s in list(str):
#         if s in list(old):
#             ret = ret + [(ord(s) - ord('a') + 1) * len(old + s)]
#             old += s
#         else:
#             old = s
#             ret = ret + [ord(s) - ord('a') + 1]
#
#     result = ['No' for _ in range(len(queries))]
#     for idx in range(len(queries)):
#         if queries[idx] in ret:
#             result[idx] = 'Yes'
#     return result

def weightedUniformStrings(str, queries):
    ret = []
    str_s = set(list(str))
    result = ['No' for _ in range(len(queries))]
    for idx, q in enumerate(queries):
        for s in str_s:
            A = ord(s) - ord('a') + 1
            if q % A == 0 and (s * (q // A)) in str:
                result[idx] = 'Yes'
                break
    return result


if __name__ == '__main__':
    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)
    print('\n'.join(result))
