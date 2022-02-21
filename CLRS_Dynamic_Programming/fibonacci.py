def fibonacci(n: int)-> int:
    """give an integer number and give the the fibonacci value
    fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

    Args:
        n (int): the index of the number

    Returns:
        int: value of the number
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)