l = [5, 7, 9, 1, 3]
for n in range(0, len(l)):
    val = l[n]
    for m in range(n, len(l)):
        if l[m] < val:
            val = l[m]
            ind = m
    l[n], l[ind] = val, l[n]
    print(l)



