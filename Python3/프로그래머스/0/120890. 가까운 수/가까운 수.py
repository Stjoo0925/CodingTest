def solution(array, n):
    x = array[0]
    for i in array:
        if abs(i - n) < abs(x - n):
            x = i
        elif abs(i - n) == abs(x - n):
            if i < x:
                x = i

    return x
