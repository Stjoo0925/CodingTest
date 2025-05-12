def solution(s):
    answer = ''
    is_first = True
    for i in s:
        if i == " ":
            answer += i
            is_first = True
        else:
            if is_first:
                answer += i.upper()
                is_first = False
            else:
                answer += i.lower()
    return answer