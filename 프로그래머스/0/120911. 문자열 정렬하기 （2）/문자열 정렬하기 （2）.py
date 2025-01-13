def solution(my_string):
    x = list(my_string)
    y = []
    for i in x:
        if i.isupper():
            y.append(i.lower())
        else:
            y.append(i)
    y = sorted(y)
    return "".join(y)