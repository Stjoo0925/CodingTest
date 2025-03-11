def solution(my_string, indices):
    x = list(my_string)
    for i in sorted(indices, reverse=True):
        x.pop(i)
    return "".join(x)