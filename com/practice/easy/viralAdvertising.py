# 21:35 start 21:47 end
# 1. 첫날은 광고의 /2 가 광고를 좋아한다.

def viralAdvertising(n):  # n 날짜
    shared = 5
    comulative = 0
    for i in range(n):
        liked = shared // 2
        comulative += liked
        if i + 1 != n:
            shared = liked * 3
    return comulative


if __name__ == '__main__':
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)
