r = 5
i = 1
while i <= r:
    j = i
    while j < r:
        
        print(' ', end=' ')
        j += 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = r
while i >= 1:
    j = i
    while j <= r:
        print(' ', end=' ')
        j += 1
    k = 1
    while k < i:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1