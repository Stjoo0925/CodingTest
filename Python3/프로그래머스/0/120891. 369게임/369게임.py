def solution(order):
    count = 0
    x = str(order)
    for i in x:
        if i in '369':
            count += 1
    
    return count