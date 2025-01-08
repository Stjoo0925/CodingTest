def solution(numbers, direction):
    if direction == "right":
        x = numbers[-1]
        del numbers[-1]
        numbers.insert(0, x)
    
    if direction == "left":
        x = numbers[0]
        del numbers[0]
        numbers.append(x)
    
    return numbers