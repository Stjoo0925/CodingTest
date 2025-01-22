def solution(arr):
    count = arr[0]
    x = []
    x.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] == count:
            count = arr[i]
        else:
            x.append(arr[i])
            count = arr[i]
    return x