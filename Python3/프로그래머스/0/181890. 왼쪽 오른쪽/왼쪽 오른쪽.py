def solution(str_list):
    idx = 0
    while idx < len(str_list):
        if str_list[idx] == "l":
            return str_list[:idx]
        elif str_list[idx] == "r":
            return str_list[idx+1:]
        idx += 1
    return []