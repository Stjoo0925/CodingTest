def solution(arr1, arr2):
    if len(arr1) == len(arr2):
        x = 0
        y = 0
        for i in arr1:
            x += i
        for j in arr2:
            y += j
        if x == y:
            return 0
        elif x > y:
            return 1
        else:
            return -1
    elif len(arr1) > len(arr2):
        return 1
    else:
        return -1
    return answer