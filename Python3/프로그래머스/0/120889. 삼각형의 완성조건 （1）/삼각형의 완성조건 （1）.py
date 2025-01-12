def solution(sides):
    x = sorted(sides)
    if x[-1] < x[-2] + x[-3]:
        return 1
    else:
        return 2