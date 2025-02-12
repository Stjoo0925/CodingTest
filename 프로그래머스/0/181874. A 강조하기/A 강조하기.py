def solution(myString):
    x = myString.lower()
    y = list(x)
    answer = []
    for i in y:
        if i == "a":
            i = i.upper()
            answer.append(i)
        else:
            answer.append(i)
    return "".join(answer)