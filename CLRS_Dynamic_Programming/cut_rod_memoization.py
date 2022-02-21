def cut_rod_memoization_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    q = -1000
    if r[n] == -1000:
        for i in range(1, n+1):
            q = max(q, p[i] + cut_rod_memoization_aux(p, n-i, r))
    r[n] = q
    return q


def cut_rod_memoization (p, n):
    # r = auxiliary list
    r = [0]
    for i in range(1, n+1):
        r.append(-1000)
    return(cut_rod_memoization_aux(p, n, r))

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 2
print(cut_rod_memoization(p, n))


