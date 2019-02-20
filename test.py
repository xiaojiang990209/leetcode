a = 1000
def isUnique(prefix, last):
    while prefix != 0:
        if prefix % 10 == last:
            return False
        prefix //= 10
    return True

unique = []
for i in range(0, a):
    if i < 10:
        unique.append(True)
    else:
        prefix = i // 10
        last = i % 10
        if unique[prefix] == True and isUnique(prefix, last):
            unique.append(True)
        else:
            unique.append(False)

for i in range(0, a):
    if unique[i] == False:
        print ("{},".format(i), end="")



