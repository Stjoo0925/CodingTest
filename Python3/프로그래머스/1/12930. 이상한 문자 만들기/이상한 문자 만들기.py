def solution(s):
    s_list = s.split(" ")
    result = []
    for i in range(len(s_list)):
        for j in range(len(list(s_list[i]))):  
            x = s_list[i]
            y = ""
            if x[j] == " ":
                result.append(x[j])
            elif j % 2 == 0:
                y = x[j].upper()
                result.append(y)   
            else:
                y = x[j].lower()
                result.append(y)
        if i != len(s_list) - 1:
            result.append(" ")
    answer = ''.join(result)
    return answer