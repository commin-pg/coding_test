# Complete the catAndMouse function below.
def catAndMouse(A, B, C):
    # A,B 고양이
    # C 쥐
    a, b = abs(A - C), abs(B - C)
    if a == b:
        return "Mouse C"
    elif a > b:
        return "Cat B"
    elif a < b:
        return "Cat A"


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        result = catAndMouse(x, y, z)
        print(result)
