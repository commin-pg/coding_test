# [Container Type] : List, Tuple, Dictionary, Set


"""
List : 리스트 자료형
"""
# List Comprehension 사용하기
list_arr = [i for i in range(1000) if i % 2 == 0]
print(list_arr)

setA = [i for i in range(1000)]
print(setA)

# sort 와 sorted 구분하기
lst = [3, 4, 2, 5, 7, 1]
print(sorted(lst))  # sorted 함수는 정렬한 값을 반환하는 함수
print(lst)

lst.sort()  # sort 메서드는 리스트를 변환
print(lst)

# len, sum, max, min 등 활용하기
s = 'abc'
print(len(s))
print(len(lst))
print(sum(lst))
print(max(lst))
print(min(lst))

# Slicing, [-1] 등 음수 인덱스 활용
lst = [0] + lst
print(lst)
lst = lst + [9]
print(lst)

lst[:3] = [8]
print(lst)
# lst[0:] = [6] <- 이건 안됨

print(lst[-1])  # 리스트의 가장 마지막
print(lst[-2])  # 리스트의 마지막부터 두번째

# reduce, filter도 활용하면 좋음

"""
Tuple 튜플 자료형
"""
# 초기 상태 표현시 코드가 길어지는 것 방지
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

# Map과 함게 사용하여 입력 받기
# a, b = map(int, input().split())
# print(a, b)

# 동시에 변해야하는 객체에 효율적 표현 가능
a, b = 3, 7
a, b = b, a
print(a, b)

"""
Dictionary 딕셔너리 자료형
"""
# key나 values를 사용하여 효율적인 사용 추천
dict_test = {1: 3, 2: 4, 'key': 7}
print(dict_test)
print(dict_test.values())
print(dict_test.keys())
# 반복문 돌리기

# 개인적으로는 무낮열 자체를 index로 사용하고 싶은 경우


"""
Set 셋 자료형
"""
# 중복체크
st = set([1, 2, 3, 4, 5, 6, 7, 87, 6, 65, 4, 4, 3, 3])
print(st)

lst = [1, 2, 3, 4, 6, 3, 3]


def isDupCheck(lst):
    return len(lst) == len(set(lst))


print(isDupCheck(lst))





# 합집합, 여집합, 차집합 등 집합 연산
