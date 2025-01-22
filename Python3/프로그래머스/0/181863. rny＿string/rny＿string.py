def solution(rny_string):
    x = list(rny_string)
    answer = []
    for i in x:
        if i == "m":
            answer.append("rn")
        else:
            answer.append(i)
    return "".join(answer)