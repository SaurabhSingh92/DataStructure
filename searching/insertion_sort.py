l1 = [5, 4,3,2,1]

for num in l1:
    j = l1.index(num)
    while j>0:
        if l1[j-1]>l1[j]:
            l1[j], l1[j-1] = l1[j-1], l1[j]
        else:
            break
        j = j-1
    print(l1)

