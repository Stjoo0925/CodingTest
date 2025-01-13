def solution(numbers):
    x = sorted(numbers)
    return x[-1] * x[-2] if x[-1] * x[-2] > x[0] * x[1] else x[0] * x[1]