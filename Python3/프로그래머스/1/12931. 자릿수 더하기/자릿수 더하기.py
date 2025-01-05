def solution(n):
    x = 0
    y = str(n)
    for i in range(len(y)):
        x += int(y[i])
    return x