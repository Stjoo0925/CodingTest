def solution(l, r):
    x = []
    for i in range(l, r + 1):
        if all(c in '05' for c in str(i)):
            x.append(i)
    return x if x else [-1]