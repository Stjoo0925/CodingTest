def solution(emergency):
    x = sorted(emergency, reverse=True)
    answer = []
    for y in emergency:
        rank = 1
        for z in x:
            if y == z:
                answer.append(rank)
                break
            rank += 1
    return answer