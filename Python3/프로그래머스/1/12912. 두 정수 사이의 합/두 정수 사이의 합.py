def solution(a, b):
    x = 0
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        x += i
    return x