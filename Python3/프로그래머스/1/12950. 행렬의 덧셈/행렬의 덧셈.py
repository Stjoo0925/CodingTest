def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        x = []
        for e in range(len(arr1[0])):
            x.append(arr1[i][e] + arr2[i][e])
        answer.append(x)
    return answer
