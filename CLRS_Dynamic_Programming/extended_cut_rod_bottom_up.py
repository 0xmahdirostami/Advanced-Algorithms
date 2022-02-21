def extended_cut_rod_bottom_up(p, n):
    r = [0 for x in range(n+1)]
    s = [0 for x in range(n+1)]
    r[0] = 0
    for j in range(1, n+1):
        q = -1000
        for i in range(1, j+1):
            if q < (p[i]+r[j-i]):
                q = p[i]+r[j-i]
                s[j] = i
        r[j] = q
        print("r:", r)
        print("s:", s)
    return r[n]


p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 10

print(extended_cut_rod_bottom_up(p, n))