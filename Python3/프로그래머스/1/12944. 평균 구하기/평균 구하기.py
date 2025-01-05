def solution(arr):
    x = 0
    for i in arr:
        x += i
    return x / len(arr)