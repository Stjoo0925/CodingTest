def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i % 2 == 0:
            x = strArr[i].lower()
            answer.append(x)
        elif i % 2 != 0:
            x = strArr[i].upper()
            answer.append(x)
    return answer