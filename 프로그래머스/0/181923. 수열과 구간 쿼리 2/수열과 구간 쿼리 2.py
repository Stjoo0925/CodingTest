def solution(arr, queries):
    result = []
    
    for query in queries:
        s, e, k = query
        value = -1
        
        for i in range(s, e + 1):
            if arr[i] > k:
                if value == -1 or arr[i] < value:
                    value = arr[i]
        
        result.append(value)
    
    return result