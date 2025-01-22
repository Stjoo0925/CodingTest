def solution(num, total):
    start = (total - (num * (num - 1) // 2)) // num
    answer = []
    for i in range(0, num):
        answer.append(start + i)
    return answer