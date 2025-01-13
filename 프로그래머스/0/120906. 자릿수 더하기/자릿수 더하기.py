def solution(n):
    x = list(str(n))
    y = 0
    for i in x:
        y += int(i)
    return y