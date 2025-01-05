def solution(n):
    x = []
    x.append(n)
    while n:
        if n == 1:
            break
        elif n % 2 == 0:
            n = int(n / 2)
            x.append(n)
        else:
            n = 3 * n + 1
            x.append(n)
    return x