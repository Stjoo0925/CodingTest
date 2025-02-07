def solution(myString, pat):
    result = list(myString)
    arr = []
    
    for i in result:
        if i == "A":
            i = "B"
        else:
            i = "A"
        arr.append(i)
        
    answer = "".join(arr)
    
    if pat in answer:
        return 1
    else:
        return 0