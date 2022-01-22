def partition(l, left, right):
    pivot = l[left]
    i = left
    j = right
    while i != j:
        while l[j] >= pivot and i < j:
            j -= 1
        l[i] = l[j]
        while l[i] <= pivot and i < j:
            i += 1
        l[j] = l[i]
    l[i] = pivot
    return i


def quickSort(l, left, right):
    pos = partition(l, left, right)
    if left < pos - 1:
        quickSort(l, left, pos - 1)
    if pos + 1 < right:
        quickSort(l, pos + 1, right)


def binaryIterative(el, l):
    if len(l) == 0:
        return 0
    if el <= l[0]:
        return 0
    if el >= l[len(l) - 1]:
        return len(l)
    left = 0
    right = len(l)
    while right - left > 1:
        m = (left + right) // 2
        if el <= l[m]:
            right = m
        elif el >= l[m]:
            left = m
    return right


def divide_impera(l):
    quickSort(l, 0, len(l)-1)  # am sortat lista
    poz = binaryIterative(0, l)  # aflam pozitia lui 0 in lista
    neg_list = l[:poz]
    return len(neg_list)
