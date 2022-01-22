# recursiv
def binaryS(el, l, left, right):
    """
     Search an element in a list
     el - element to be searched; l - a list of ordered elements
     left,right the sublist in which we search return the position of first occurrence or the insert position
     """
    if left >= right - 1:
        return right
    m = (left + right) // 2
    if el <= l[m]:
        return binaryS(el, l, left, m)
    else:
        return binaryS(el, l, m, right)


def binarySearchRec(el, l):
    """
     Search an element in a list
     el - element to be searched
     l - a list of ordered elements
     return the position of first occurrence or the insert position
     """
    if len(l) == 0:
        return 0
    elif el < l[0]:
        return 0
    elif el > l[len(l) - 1]:
        return len(l)
    binaryS(el, l, 0, len(l))


# iterativ
def binarySIterative(el, l):
    """
    Search an element in a list
    el - element to be searched
    l - a list of ordered elements
    return the position of first occurrence or the position where the element can be inserted
    """
    if len(l) == 0:
        return 0
    elif el <= l[0]:
        return 0
    elif el >= l[len(l) - 1]:
        return len(l)
    right = len(l) - 1
    left = 0
    while right - left > 1:
        m = (left + right) // 2
        if el <= l[m]:
            right = m - 1
        else:
            left = m + 1
    return right
