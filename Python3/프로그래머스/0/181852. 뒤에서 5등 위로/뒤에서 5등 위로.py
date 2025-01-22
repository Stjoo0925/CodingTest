def solution(num_list):
    x = sorted(num_list)
    answer = []
    for i in range(5, len(num_list)):
        answer.append(x[i])
    return answer