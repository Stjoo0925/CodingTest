def solution(num_list, n):
    x = len(num_list)
    y = int(x/n)
    z = []
    zz = []
    j = 0
    for i in range(0, y):
        for e in range(j, j+n):
            z.append(num_list[e])
        zz.append(z)
        z = []
        j += n
    return zz