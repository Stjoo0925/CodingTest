def solution(price):
    if price >= 500000:
        dis = 0.8
    elif price >= 300000:
        dis = 0.9
    elif price >= 100000:
        dis = 0.95
    else: dis = 1
    return int(price * dis)