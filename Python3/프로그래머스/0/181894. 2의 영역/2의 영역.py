def solution(arr):
    arr_2 = []
    answer = []
    for i in range(len(arr)):
        if arr[i] == 2:
            arr_2.append(i)
    if arr_2 == []:
        return [-1]
    for i in range(arr_2[0], arr_2[-1]+1):
        answer.append(arr[i])
    return answer