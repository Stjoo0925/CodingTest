def solution(my_string):
    answer = [0] * 52

    for ch in my_string:
        if 'A' <= ch <= 'Z':
            index = ord(ch) - ord('A')
        elif 'a' <= ch <= 'z':
            index = ord(ch) - ord('a') + 26
        else:
            continue
        answer[index] += 1

    return answer
