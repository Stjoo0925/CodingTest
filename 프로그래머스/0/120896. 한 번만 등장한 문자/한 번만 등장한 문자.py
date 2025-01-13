def solution(s):
    x = sorted(list(s))
    y = []
    for i in x:
        z = x.count(i)
        if z == 1:
            y.append(i)
    return "".join(y)