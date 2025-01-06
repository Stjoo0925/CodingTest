def solution(x):
    y = str(x)
    z = 0
    for i in range(len(y)):
        z += int(y[i])
    if x % z == 0:
        return True
    return False