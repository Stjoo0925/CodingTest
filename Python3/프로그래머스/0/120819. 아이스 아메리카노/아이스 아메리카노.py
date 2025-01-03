def solution(money):
    a = int(money / 5500)
    b = money - (a * 5500)
    c = [a, b]
    return c