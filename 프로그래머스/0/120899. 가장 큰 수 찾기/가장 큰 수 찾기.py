def solution(array):
    x = 0
    for i in array:
        if i > x:
            x = i
    y = array.index(x)
    return [x,y]