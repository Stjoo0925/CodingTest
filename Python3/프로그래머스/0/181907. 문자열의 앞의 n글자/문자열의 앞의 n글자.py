def solution(my_string, n):
    x = list(my_string)
    answer = ""
    for i in range(0, n):
        answer += x[i]
    return answer