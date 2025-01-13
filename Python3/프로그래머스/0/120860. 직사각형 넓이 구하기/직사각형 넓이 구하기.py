def solution(dots):
    x = 0
    x_arr = []
    y = 0
    y_arr = []
    for i in dots:
        x_arr.append(i[0])
        y_arr.append(i[1])
    x_min = min(x_arr)
    x_max = max(x_arr)
    y_min = min(y_arr)
    y_max = max(y_arr)
    x = x_max - x_min
    y = y_max - y_min
    return x * y