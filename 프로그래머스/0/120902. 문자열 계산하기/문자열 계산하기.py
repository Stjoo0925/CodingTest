def solution(my_string):
    x = my_string.split()
    y = int(x[0])
    for i in range(1, len(x)):
        if x[i] == '+':
            y += int(x[i+1])
        elif x[i] == '-':
            y -= int(x[i+1])
    return y