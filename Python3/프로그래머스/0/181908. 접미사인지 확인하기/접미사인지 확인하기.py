def solution(my_string, is_suffix):
    if len(is_suffix) > len(my_string):
        return 0
    
    for i in range(len(is_suffix)):
        if my_string[len(my_string)-len(is_suffix)+i] != is_suffix[i]:
            return 0
    return 1