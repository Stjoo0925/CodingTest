def solution(num, total):
    y = num // 2
    if total % num == 0:
        x = total // num
    else:
        x = total // num + 1
    start = x - y
    answer = []
    for i in range(0, num):
        answer.append(start + i)
    return answer