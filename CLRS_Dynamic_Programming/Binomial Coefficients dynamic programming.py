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
    matrix = [[0 for x in range(k+1)] for x in range(n+1)]

    # Coefficient in bottom up manner
    for i in range(n+1):
        for j in range(min(i, k)+1):
            # Base Cases
            if j == 0 or j == i:
                matrix[i][j] = 1
  
            # Calculate value using
            # previously stored values
            else:
                matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]
  
    return matrix[n][k]
