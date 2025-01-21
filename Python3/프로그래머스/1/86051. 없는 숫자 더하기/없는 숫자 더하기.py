def solution(numbers):
    x = [0,1,2,3,4,5,6,7,8,9]
    y = 0
    for i in x:
        if i not in numbers:
            y += i
    return y