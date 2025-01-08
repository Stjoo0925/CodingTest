def solution(n):
    x = True
    count = 1
    i = 1
    while x:
        i = count * i
        if i > n:
            x = False
        if i <= n:
            count += 1
    return count - 1