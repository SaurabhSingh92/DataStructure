def merge_sort(lst):
    while len(lst) <= 1:
        return lst

    left_list, right_list = split(lst)
    left = merge_sort(left_list)
    right = merge_sort(right_list)

    return merge(left, right)


def split(l):
    mid = len(l) // 2
    left = l[:mid]
    right = l[mid:]
    return left, right


def merge(left, right):
    tmp=[]
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            tmp.append(left[i])
            i+=1
        else:
            tmp.append(right[j])
            j+= 1

    while i < len(left):
        tmp.append(left[i])
        i+=1

    while j < len(right):
        tmp.append(right[j])
        j+=1

    return tmp


if __name__ == '__main__':
    l = [4, 3, 6, 9, 1]
    print(merge_sort(l))
