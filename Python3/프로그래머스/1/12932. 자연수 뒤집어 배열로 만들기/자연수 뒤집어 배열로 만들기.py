def solution(n):
    x = str(n)
    y = []
    for i in range(len(x)):
        z = int(x[i])
        y.append(z)
    y.reverse()
    return y