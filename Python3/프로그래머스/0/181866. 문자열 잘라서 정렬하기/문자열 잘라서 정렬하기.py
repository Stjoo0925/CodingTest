def solution(myString):
    result = sorted(myString.split("x"))
    while "" in result:  
        result.remove("")
    return result
