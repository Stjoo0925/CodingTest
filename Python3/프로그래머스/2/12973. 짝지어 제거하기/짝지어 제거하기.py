def solution(s):
    arr = []
    for i in s:
        if arr and arr[-1] == i:
            arr.pop()
        else:
            arr.append(i)
    return 1 if not arr else 0
