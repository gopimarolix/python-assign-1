s1 = 1
s2 = 2
n = s2
for row in range(2, 6):
    for col in range(s1, s2):
        n -= 1
        print(n, end=' ')
    print("")
    s1 = s2
    s2 += row
    n = s2