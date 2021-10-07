"""
[Integer 정수 자료형]
"""

a = 1
print(a)

print(2 ** 1000)  # 파이썬은 수의 크기에 제한이 없다.

print(str(123))  # 문자열로 쉽게 바꿀 수 있다.

print(type(3 / 3))  # 나누기 연산 하나만 사용하면, float 자료형으로 떨어진다.

print(type(3 // 3))  # 나누기 연산 두개를 사용하면, int 자료형으로 떨어진다.

print(divmod(7, 3), type(divmod(7, 3)))  # 몫과 나머지를 한번에 구해준다. (tuple로 떨어진다.)

"""
[Float 실수 자료형]
"""


print(0.1 * 3 == 0.3)  # 일단 연산에서는 쓰지말자. 0.1 * 3 == 0.3 # False  : Decimal 을 사용 또는 실수 오차를 해결할 자신있을때만 사용

print((1, 3), (2, 3))


"""
[String 문자열 자료형]
"""


#  Immutable 변수
#   - List로 변환하여 사용하기
s = "an commin"
for i in s:
    i = 'c'
print(s)
# for i in range(0, len(s)):
#    s[i] = "d"
# print(s)

# + 연산과 * 연산 조심하기
s = 'abc'
b = 'dfg'
print(s + b)

#  -join() method 활용하기
s = ''
for i in range(10000):  # 실행속도 5.96 us
    s = s + str(i)

s = ''
s = s.join([str(i) for i in range(10000)])  # 실행속도 5.01 us

# .split() .replace() 등 다양한 method 활용이 초점
# Slicing 을 자유롭게 할 수 있는 것

s = 'abcd'
print(s[:1])  # 첫번째 문자까지 슬라이스
print(s[2:])  # 끝에서 두번째 문자까지 슬라이스

# Char 를 ord와 chr 로 다루기
print(chr(65))
print(ord('A'))

# 논리 연산과 활용

# Short Circuit
#   - or 연산에 앞 항이 참
# if 0 and (1 // 0) == 0:
#     print('hello')

if 1 and 0:
    print('hello')
if 1 or 0:
    print('hello2')

#   - and 연산에 앞 항이 거짓
# 모든 문제의 기본 : 참/ 거짓

