def solution(s):
    x = {}
    answer = []
    for index, num in enumerate(s):
        if num not in x:
            answer.append(-1)
        else:
            answer.append(index - x[num])
        x[num] = index
    return answer
