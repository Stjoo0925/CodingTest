def solution(arr):
    x = len(arr)
    n = 0
    while (2 ** n) < x:
        n += 1
    arr.extend([0] * (2 ** n - x))
    return arr