def solution(n):
    arr = []
    for num in range(1, n + 1):
        if num % 2 == 1:
            arr.append(num)
    return arr