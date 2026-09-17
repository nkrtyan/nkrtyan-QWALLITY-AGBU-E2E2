def quick_sort(lst):
    if len(lst)<=1:
        return lst
    pivot=lst[0]
    left=[x for x in lst[1:] if x<=pivot]
    right=[x for x in lst[1:] if x>pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)
list=[5,2,8,1,9]
print(quick_sort(list))