def solution(myStr):
    x = ""
    answer = []
    
    for i in myStr:
        if i in "abc":
            if x != "":
                answer.append(x)
            x = ""
        else:
            x += i
    
    if x != "":
        answer.append(x)
    
    if not answer:
        return ["EMPTY"]
    
    return answer