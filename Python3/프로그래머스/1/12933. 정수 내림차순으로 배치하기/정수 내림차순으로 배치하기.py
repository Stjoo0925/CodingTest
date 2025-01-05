def solution(n):
    x = str(n)
    y = []
    for i in range(len(x)):
        z = x[i]
        y.append(z)
    y.sort()
    y.reverse()
    xx = ""
    for i in range(len(y)):
        xx += y[i]
    return int(xx)