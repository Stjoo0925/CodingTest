def solution(n, t):
    count = 1
    while True:
        n = n * 2
        if t == count:
            break
        count += 1
    return n