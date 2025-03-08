def solution(arr, intervals):
    answer = []
    for i in intervals:
        for e in range(i[0], i[1]+1):
            answer.append(arr[e])
    return answer