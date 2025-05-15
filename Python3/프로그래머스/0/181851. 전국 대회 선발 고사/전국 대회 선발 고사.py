def solution(rank, attendance):
    x = []

    for i in range(len(rank)):
        if attendance[i]:
            x.append((rank[i], i))

    x.sort()

    a = x[0][1]
    b = x[1][1]
    c = x[2][1]

    return 10000 * a + 100 * b + c