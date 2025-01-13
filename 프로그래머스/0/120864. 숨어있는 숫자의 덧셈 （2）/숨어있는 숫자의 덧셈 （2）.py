def solution(my_string):
    sum = 0
    num = ""
    for char in my_string:
        if char.isdigit():
            num += char
        else:
            if num:
                sum += int(num)
                num = ""
    if num:
        sum += int(num)
    return sum