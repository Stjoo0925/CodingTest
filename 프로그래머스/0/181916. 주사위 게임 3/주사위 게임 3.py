from collections import Counter

def solution(a, b, c, d):
    roll = [a, b, c, d]
    count = Counter(roll)
    
    if len(count) == 1:
        return 1111 * roll[0]
    
    if len(count) == 2 and 3 in count.values():
        p = [key for key, value in count.items() if value == 3][0]
        q = [key for key, value in count.items() if value == 1][0]
        return (10 * p + q) ** 2
    
    if len(count) == 2 and 2 in count.values():
        p, q = [key for key, value in count.items() if value == 2]
        return (p + q) * abs(p - q)
    
    if len(count) == 3:
        p = [key for key, value in count.items() if value == 2][0]
        remaining = [key for key, value in count.items() if value == 1]
        q, r = remaining
        return q * r
    
    return min(roll)
