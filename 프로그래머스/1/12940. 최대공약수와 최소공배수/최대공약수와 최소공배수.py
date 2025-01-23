def solution(n, m):
    n_divisor = []
    m_divisor = []
    divisor = []
    gcd = 0
    lcm = 0
    for i in range(1, n+1):
        if n % i == 0:
            n_divisor.append(i)
    for i in range(1, m+1):
        if m % i == 0:
            m_divisor.append(i)
    for i in n_divisor:
        if i in m_divisor:
            divisor.append(i)
    gcd = max(divisor)
    lcm = (n * m) // gcd
    return [gcd, lcm]