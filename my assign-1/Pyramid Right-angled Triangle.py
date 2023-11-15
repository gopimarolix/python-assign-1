r = 6
for row in range(1, r):
    n = 1
    for j in range(r, 0, -1):
        if j > row:
            print(" ", end=' ')
        else:
            print(n, end=' ')
            n += 1
    print("")