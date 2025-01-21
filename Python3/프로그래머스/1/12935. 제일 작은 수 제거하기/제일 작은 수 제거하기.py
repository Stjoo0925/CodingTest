def solution(arr):
    x = min(arr)
    y = []
    if arr == [10]:
        y.append(-1)
    else:
        for i in arr:
            if i != x:
                y.append(i)
    return y