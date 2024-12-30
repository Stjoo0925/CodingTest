def solution(numbers):
    answer = [0] * len(numbers)
    for i in range(len(numbers)):
        answer[i] = 2 * numbers[i]
    return answer