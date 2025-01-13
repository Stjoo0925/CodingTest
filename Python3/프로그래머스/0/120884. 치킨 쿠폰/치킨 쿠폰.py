def solution(chicken):
    x = 0
    y = chicken
    
    while y >= 10:
        new_chicken = y // 10
        x += new_chicken
        y = new_chicken + (y % 10)
    
    return x
