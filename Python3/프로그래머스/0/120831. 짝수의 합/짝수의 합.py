def solution(n):
    x = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            x += i
    return x