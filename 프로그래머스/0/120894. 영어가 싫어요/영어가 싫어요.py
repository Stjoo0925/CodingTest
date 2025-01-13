def solution(numbers):
    di = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, 
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    
    answer = ""
    x = ""
    
    for i in numbers:
        x += i
        if x in di:
            answer += str(di[x])
            x = ""
    
    return int(answer)
