def solution(s):
    x = list(s)
    y = len(x) // 2
    if len(x) % 2 == 0:
        return x[y-1] + x[y]
    else:
        return x[y] 