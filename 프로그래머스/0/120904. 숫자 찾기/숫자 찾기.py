def solution(num, k):
    x = list(str(num))
    y = str(k)
    if y in x:
        return x.index(y) + 1
    else:
        return -1