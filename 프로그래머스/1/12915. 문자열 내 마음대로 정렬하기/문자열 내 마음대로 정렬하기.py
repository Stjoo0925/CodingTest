def solution(strings, n):
    arr1 = []
    for s in strings:
        arr1.append((s[n], s))

    arr1.sort()

    result = [s for _, s in arr1]
    return result