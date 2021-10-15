l1 = [2,1,3,4,5]

for rng in range(1, len(l1)):
    lmt = len(l1) - rng
    ind = 'N'
    for num in range(0, lmt):
        if l1[num] > l1[num + 1]:
            tmp = l1[num + 1]
            l1[num + 1] = l1[num]
            l1[num] = tmp
            ind = 'Y'
    print(l1)
    if ind == 'N':
        break


