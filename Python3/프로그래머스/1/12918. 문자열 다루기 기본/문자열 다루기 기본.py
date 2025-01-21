def solution(s):
    num = ["0","1","2","3","4","5","6","7","8","9"]
    x = list(s)
    y = True
    if len(x) == 4 or len(x) == 6:
        for i in x:
            if i not in num:
                y = False
                break
            else:
                y = True
    else:
        return False
                
    return y