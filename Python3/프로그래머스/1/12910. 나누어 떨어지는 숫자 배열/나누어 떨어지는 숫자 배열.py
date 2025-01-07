def solution(arr, divisor):
    x = []
    y = sorted(arr)
    for i in range(len(y)):
        if y[i] % divisor == 0:
            x.append(y[i])
    if len(x) == 0:
        x.append(-1)
    return x