def solution(s1, s2):
    x = 0
    for i in s1:
        if i in s2:
            x += 1
    return x