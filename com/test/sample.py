def fizzBuzz(n):
    for i in range(1, n + 1):
        s = ''
        if i % (3 * 5) is 0:
            s = 'FizzBuzz'
        elif i % 3 is 0:
            s = 'Fizz'
        elif i % 5 is 0:
            s = 'Buzz'
        else:
            s = str(i)
        print(s)


if __name__ == '__main__':
    """ 
    1. i 가 3과 5의 배수라면, FizBuzz 를 인쇄
    2. i가 3의 배수인 경우 Fizz
    3. i가 5의 배수라면, Buzz
    4. i가 3,5의 배수가 아니라면, i의 값을 출력 
    """
    N = int(input())
    fizzBuzz(N)
