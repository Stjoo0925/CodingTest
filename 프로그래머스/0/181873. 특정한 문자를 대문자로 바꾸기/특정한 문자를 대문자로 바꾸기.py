def solution(my_string, alp):
    x = list(my_string)
    answer = []
    for i in x:
        if i == alp:
            i = i.upper()
            answer.append(i)
        else:
            answer.append(i)
    return "".join(answer)