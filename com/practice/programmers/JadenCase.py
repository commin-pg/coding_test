def solution(s):
    s = s.lower()
    answer = []

    for ss in s.split(' '):
        answer.append(ss.capitalize())  # CamelCase로 변경

    return ' '.join(answer)


arr = ["3people unFollowed me", "for the last week", "a"]
for a in arr:
    print(solution(a))
