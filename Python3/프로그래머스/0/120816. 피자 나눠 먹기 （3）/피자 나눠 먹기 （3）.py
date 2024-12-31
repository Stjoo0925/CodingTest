def solution(slice, n):
    count = 1
    while (count * slice) / n < 1:
        count += 1
    return count