def solution(myString):
    x = list(myString)
    answer = ""
    for i in x:
        if ord(i) < ord("l"):
            answer += "l"
        else:
            answer += i
    return answer