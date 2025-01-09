def solution(my_string):
    answer = ""
    mo = {"a", "e", "i", "o", "u"}
    for i in range(len(my_string)):
        if my_string[i] not in mo:
            answer += my_string[i]
    return answer