def solution(my_string):
    x = set()
    y = []
    
    for i in my_string:
        if i not in x:
            x.add(i)
            y.append(i)
    
    answer = ""
    for i in y:
        answer += i
    
    return answer