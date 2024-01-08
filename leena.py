s = "ABCCCDDDEFGGGHHHIIJJKLLABCDEF"
l = ""
for c in s:
    if c not in l:
        l = l+c
print(l)
#k = list("ABCCCDDDEFGGGHHHIIJJKLLABCDEF")