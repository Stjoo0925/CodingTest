def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        count = 0
        for e in range(1, i + 1):
            if i % e == 0:
                count += 1
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
