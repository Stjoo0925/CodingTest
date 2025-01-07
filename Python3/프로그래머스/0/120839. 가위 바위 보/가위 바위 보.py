def solution(rsp):
    x = ''
    for i in rsp:
        if i == '2':
            x += '0'
        elif i == '0':
            x += '5'
        else:
            x += '2'
    return x