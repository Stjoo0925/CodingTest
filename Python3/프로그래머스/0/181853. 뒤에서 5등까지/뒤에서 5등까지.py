def solution(num_list):
    answer = []
    x = sorted(num_list)
    for i in range(5):
        answer.append(x[i])
    return answer