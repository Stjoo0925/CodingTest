def solution(s):
    s_arr = list(map(int, s.split()))
    a = max(s_arr)
    b = min(s_arr)
    
    return str(b) + " " + str(a)