def solution(sizes):
    x, y = 0, 0
    for w, h in sizes:
        if w < h:
            w, h = h, w
        x = max(x, w)
        y = max(y, h)
    return x * y
