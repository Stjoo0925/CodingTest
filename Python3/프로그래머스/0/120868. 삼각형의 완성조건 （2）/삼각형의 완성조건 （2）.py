def solution(sides):
    count = 0
    for x in range(max(sides) - min(sides) + 1, max(sides) + 1):
        count += 1
    for x in range(max(sides) + 1, min(sides) + max(sides)):
        count += 1
    return count
