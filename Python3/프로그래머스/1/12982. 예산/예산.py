def solution(d, budget):
    d_sort = sorted(d)
    count = 0
    i = 0
    while budget != 0 and i < len(d_sort):
        if budget - d_sort[i] >= 0:
            budget = budget - d_sort[i]
            i += 1
            count += 1
        else:
            break
    return count