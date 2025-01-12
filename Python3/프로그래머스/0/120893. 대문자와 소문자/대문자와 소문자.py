def solution(my_string):
    x = ""
    for i in my_string:
        if i.isupper():
            x += i.lower()
        else:
            x += i.upper()
    return x
