def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
    if len(answer) > k:
        for i in range(len(answer) - k):
            answer.pop()
    if len(answer) < k:
        for i in range(k - len(answer)):
            answer.append(-1)
    return answer