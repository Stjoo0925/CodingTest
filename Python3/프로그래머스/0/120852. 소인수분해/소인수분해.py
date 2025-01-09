def solution(n):
    x = set()
    y = 2

    while y <= n:
        if n % y == 0:
            x.add(y)
            n //= y
        else:
            y += 1

    return sorted(x)