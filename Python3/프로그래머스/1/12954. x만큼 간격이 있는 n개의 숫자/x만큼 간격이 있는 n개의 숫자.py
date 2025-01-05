def solution(x, n):
    y = []
    for i in range(1, n+1):
        z = x * i
        y.append(z)
    return y