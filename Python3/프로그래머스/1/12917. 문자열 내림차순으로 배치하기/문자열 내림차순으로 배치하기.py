def solution(s):
    x = list(s)
    x = sorted(x, reverse = True)
    return "".join(x)