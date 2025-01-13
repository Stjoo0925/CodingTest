def solution(n):
    x = int(n ** 0.5)
    if x * x == n:
        return 1
    else:
        return 2