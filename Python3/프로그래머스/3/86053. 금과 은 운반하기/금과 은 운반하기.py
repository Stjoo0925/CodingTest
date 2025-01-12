def solution(a, b, g, s, w, t):
    left, right = 0, 10**15
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        total_gold, total_silver, total_combined = 0, 0, 0
        
        for i in range(len(g)):
            round_trip = mid // (2 * t[i])
            if mid % (2 * t[i]) >= t[i]:
                round_trip += 1
            
            max_gold = min(round_trip * w[i], g[i])
            max_silver = min(round_trip * w[i], s[i])
            max_combined = min(round_trip * w[i], g[i] + s[i])
            
            total_gold += max_gold
            total_silver += max_silver
            total_combined += max_combined
        
        if total_gold >= a and total_silver >= b and total_combined >= a + b:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer
