def solution(num_list):
    x = range(len(num_list))
    y = []
    for i in x:
        y.append(num_list[-i-1])
    return y