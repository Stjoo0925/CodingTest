def solution(n):
    def div(num):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        return count

    answer = 0
    for i in range(1, n + 1):
        if div(i) >= 3:
            answer += 1
    return answer