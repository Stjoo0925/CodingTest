def solution(my_string):
    arr = my_string.split(" ")
    answer = []
    
    for i in arr:
        if i != "":
            answer.append(i)
        
    return answer