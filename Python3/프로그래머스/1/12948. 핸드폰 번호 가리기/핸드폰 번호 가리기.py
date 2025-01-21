def solution(phone_number):
    x = list(phone_number)
    y = len(phone_number) - 4
    for i in range(0, y):
        x[i] = "*"
    return "".join(x)