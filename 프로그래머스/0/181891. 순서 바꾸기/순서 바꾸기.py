def solution(num_list, n):
    arr1 = []
    arr2 = []
    for i in range(len(num_list)):
        if i < n:
            arr1.append(num_list[i])
        else:
            arr2.append(num_list[i])
    return arr2 + arr1