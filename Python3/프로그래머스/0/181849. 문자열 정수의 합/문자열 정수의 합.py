def solution(num_str):
    x = list(num_str)
    answer = 0
    for i in x:
        answer += int(i)
    return answer