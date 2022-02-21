def cut_rod_bottom_up(p, n):
    r = [0 for x in range(n+1)]
    r[0] = 0
    for j in range(1, n+1):
        q = -1000
        for i in range(1, j+1):
            q = max(q, p[i]+r[j-j])
        r[j] = q
        print("r:", r)
    return r[n]

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 10

print(cut_rod_bottom_up(p, n))