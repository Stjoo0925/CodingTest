def solution(myString, pat):
    answer = 0
    start = 0
    
    while True:
        start = myString.find(pat, start)
        
        if start == -1:
            break
        
        answer += 1
        start += 1
    
    return answer
