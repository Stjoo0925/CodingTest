def solution(quiz):
    answer = []
    for i in quiz:
        x = i.split()
        y = int(x[0])
        for i in range(1, len(x)):
            if x[i] == '+':
                y += int(x[i+1])
            elif x[i] == '-':
                y -= int(x[i+1])
        if y == int(x[-1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer