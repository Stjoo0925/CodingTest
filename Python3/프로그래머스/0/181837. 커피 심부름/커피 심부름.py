def solution(order):
    answer = 0
    for i in order:
        if "americano" in i:
            answer += 4500
        elif "anything" in i:
            answer += 4500
        else:
            answer += 5000
    return answer