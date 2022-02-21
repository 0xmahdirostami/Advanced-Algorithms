def fibonacci(n: int)-> int:
    """give an integer number and give the the fibonacci value
    fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

    Args:
        n (int): the index of the number

    Returns:
        int: value of the number
    """
    num_list = [0, 1]
    for i in range(2, n+1):
        num_list.append(num_list[i-1] + num_list[i-2])
    return num_list[n]
