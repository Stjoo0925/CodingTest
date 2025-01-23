def solution(t, p):
    t = list(t)
    p_list = list(p)
    x = []
    for i in range(0, len(t) - len(p_list) + 1):
        x.append("".join(t[i:i + len(p_list)]))
    count = 0
    for i in x:
        if int(i) <= int(p):
            count += 1
    return count