def solution(n):
    count = 1
    while count:
        if n > 7 * count:
            count += 1
        else:
            break
    return count