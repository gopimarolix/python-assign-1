s = 7
asciiNumber = 65
m = (2 * s) - 2
for i in range(0, s):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        character = chr(asciiNumber)
        print(character, end=' ')
        asciiNumber += 1
    print(" ")