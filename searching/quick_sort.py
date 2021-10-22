def quick_sort(nums, start=0, end=None):
    if end is None:
        nums = list(nums)
        end = len(nums)-1
    if start < end:
        pivot = partition(nums, start, end)
        quick_sort(nums, start, pivot-1)
        quick_sort(nums, pivot+1, end)
    return nums


def partition(nums, s=0, e=None):
    if e is None:
        e = len(nums) - 1

    l, r = s, e - 1
    while r > l:
        if nums[l] <= nums[e]:
            l += 1
        elif nums[r] > nums[e]:
            r -= 1
        else:
            nums[l], nums[r] = nums[r], nums[l]


    if nums[l] > nums[e]:
        nums[l], nums[e] = nums[e], nums[l]
        return l
    else:
        return e


lst = [6, 3, 9, 1, 8, 4, 5, 2]

print(quick_sort(lst))
