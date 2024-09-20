def bubble_sort(first_lst):
    if len(first_lst) == 0:
        return []
    lst = []
    for i in first_lst:
        if i not in lst:
            lst.append(i)

    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] < lst[j+1]:
                tmp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = tmp
    return lst
