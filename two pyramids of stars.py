r = 6
for i in range(0, r):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")

print(" ")

for i in range(r + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")