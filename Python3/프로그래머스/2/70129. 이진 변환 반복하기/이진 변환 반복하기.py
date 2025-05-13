def solution(s):
    count = 0
    zero_cnt = 0

    while s != "1":
        zero_cnt += s.count('0')
        s = s.replace('0', '')
        s = format(len(s), 'b')
        count += 1

    return [count, zero_cnt]