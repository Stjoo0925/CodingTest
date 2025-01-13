def solution(my_str, n):
    x = list(my_str)
    y = ""
    z = []
    for i in x:
        y += i
        if len(y) == n:
            z.append(y)
            y = ""
    if y:
        z.append(y)
    return z