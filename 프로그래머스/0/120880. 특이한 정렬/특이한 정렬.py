def solution(numlist, n):
    def sort_key(x):
        return (abs(x - n), -x)

    return sorted(numlist, key=sort_key)
