def solution(k, score):
    hall = []
    result = []
    for s in score:
        hall.append(s)
        hall.sort(reverse=True)
        if len(hall) > k:
            hall.pop()
        result.append(hall[-1])
    return result
