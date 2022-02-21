def cut_rod(p: list, n: int)->int:
    """calculate the max revenue by the most efficient way of cutting

    Args:
        p (list): the price of the rod with length i
        n (int): the total length of the rod

    Returns:
        int: return a maximum revenue
    """
    if n == 0:
        return 0
    q = -10000
    for i in range(1, n+1):
        q = max(q, p[i]+cut_rod(p, n-i))
    return q
    
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 10
print(cut_rod(p, n))