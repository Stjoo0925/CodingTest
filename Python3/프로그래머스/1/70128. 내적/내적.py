def solution(a, b):
    answer = 0
    for x, y in zip(a, b):
        z = x * y
        answer += z
    return answer