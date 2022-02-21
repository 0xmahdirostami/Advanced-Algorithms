def b_c(n: int, k: int)-> int:

    """give two integer numbers and give the the biomial coefficient value
    In mathematics, the binomial coefficients are the positive integers that occur 
    as coefficients in the binomial theorem. Commonly, a binomial coefficient is 
    indexed by a pair of integers n ≥ k ≥ 0 and is written 
    {\displaystyle {\tbinom {n}{k}}.}{\displaystyle {\tbinom {n}{k}}.} 
    It is the coefficient of the xk term in the polynomial expansion of 
    the binomial power (1 + x)n, and is given by the formula
    n!/k!(n-k)!

    Returns:
        int: value of Binomial Coefficient C(n, k)
    """
    if k == 0 or k == n:
        return 1
    return b_c(n-1, k-1) + b_c(n-1, k)
