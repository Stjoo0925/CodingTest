def solution(box, n):
    a,b,c = box
    x = a // n
    y = b // n
    z = c // n
    return x * y * z