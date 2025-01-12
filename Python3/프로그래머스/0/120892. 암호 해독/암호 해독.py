def solution(cipher, code):
    x = 1
    y = ""
    while (x * code) - 1 < len(cipher):
        y += cipher[(x * code) - 1]
        x += 1
    return y