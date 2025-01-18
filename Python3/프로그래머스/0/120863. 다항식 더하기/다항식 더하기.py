def solution(polynomial):
    terms = polynomial.split(" + ")
    
    variable_coefficient = 0
    constant = 0

    for term in terms:
        if 'x' in term:
            if term == 'x':
                variable_coefficient += 1
            else:
                variable_coefficient += int(term.replace('x', ''))
        else:
            constant += int(term)

    result = []
    if variable_coefficient:
        if variable_coefficient == 1:
            result.append("x")
        else:
            result.append(f"{variable_coefficient}x")
    if constant:
        result.append(str(constant))

    return " + ".join(result)
