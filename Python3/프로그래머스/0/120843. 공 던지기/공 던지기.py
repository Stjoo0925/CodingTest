def solution(numbers, k):
    x = (2 * (k - 1)) % len(numbers)
    return numbers[x]