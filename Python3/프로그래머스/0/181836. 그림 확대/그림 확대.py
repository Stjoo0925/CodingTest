def solution(picture, k): 
    result = []
    for i in picture:
        x = ''.join(char * k for char in i)
        for _ in range(k):
            result.append(x)
    return result