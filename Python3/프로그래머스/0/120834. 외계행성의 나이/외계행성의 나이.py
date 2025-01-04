def solution(age):
    x = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    y = str(age)
    for z in y:
        result += x[int(z)]
    return result