def solution(s):
    x = s.split()
    y = []
    for i in x:
        if i == "Z":
            if y:
                y.pop()
        else:
            y.append(int(i))
    return sum(y)
