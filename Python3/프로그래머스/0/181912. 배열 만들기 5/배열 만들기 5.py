def solution(intStrs, k, s, l):
    result = []
    for string in intStrs:
        num = int(string[s:s+l])
        if num > k:
            result.append(num)
    return result
