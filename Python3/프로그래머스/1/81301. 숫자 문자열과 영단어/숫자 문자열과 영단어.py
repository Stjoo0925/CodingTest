def solution(s):
    num_map = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    
    x = list(s)
    y = []
    num = ""
    
    for i in x:
        if i.isdigit():
            if num in num_map:
                y.append(num_map[num])
                num = ""
            y.append(i)
        else:
            num += i
            if num in num_map:
                y.append(num_map[num])
                num = ""

    if num in num_map:
        y.append(num_map[num])
    
    answer = "".join(y)
    return int(answer)
