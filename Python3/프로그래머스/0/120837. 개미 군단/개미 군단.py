def solution(hp):
    x = 0
    y = 0
    z = 0
    while hp != 0:
        if hp >= 5:
            hp = hp - 5
            x += 1
        elif hp >= 3:
            hp = hp - 3
            z += 1
        else:
            hp = hp -1
            y += 1
    return x + y + z