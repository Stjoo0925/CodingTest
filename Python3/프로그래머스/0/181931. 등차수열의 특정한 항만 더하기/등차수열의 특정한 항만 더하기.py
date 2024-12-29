def solution(a, d, included):
    result = 0
    for i, include in enumerate(included):
        x = a + i * d
        if include:
            result += x
    return result