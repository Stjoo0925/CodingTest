def solution(arr):
    stk = []
    i = 0
    arr_len = len(arr)
    while i < int(arr_len):
        if stk == []:
            stk.append(arr[i])
            i += 1
        elif stk[-1] == arr[i]:
            stk.pop()
            i += 1
        elif stk[-1] != arr[i]:
            stk.append(arr[i])
            i += 1
    if stk == []:
        return [-1]
    return stk