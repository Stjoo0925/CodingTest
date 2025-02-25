def solution(a, b):
    if a % 2 != 0:
        if b % 2 != 0:
            return a ** 2 + b ** 2
        else:
            return 2 * ( a + b )
    else:
        if b % 2 != 0:
            return 2 * ( a + b )
        else:
            if a < b:
                return b - a
            else:
                return a - b