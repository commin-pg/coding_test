# 22:50 start 23:11 end

def superDigit(n):
    if len(n) == 1:
        return n
    else:
        nn = sum(list(map(int, list(n))))
        return superDigit(str(nn))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(str(sum(list(map(int, list(n)))) * k))
    print(result)
