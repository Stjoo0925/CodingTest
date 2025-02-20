def solution(my_string, is_prefix):
    answer = ""
    x = list(my_string)
    for i in x:
        answer += i
        if answer == is_prefix:
            return 1
    return 0