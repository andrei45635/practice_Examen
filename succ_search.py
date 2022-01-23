# chei ne-ordonate
def searchSucc(el, l):
    """
     Search for an element in a list
     el - element
     l - list of elements
     return the position of first occurrence or -1 if the element is not in l
    """
    i = 0
    while i < len(l) and el != l[i]:
        i += 1
    if i < len(l):
        return i
    return -1


# chei ordonate
def searchSuccOrdered(el, l):
    """
     Search for an element in a list
     el - element
     l - list of ordered elements
     return the position of first occurrence or the position where the element can be inserted
     """
    if len(l) <= 0:
        return -1
    if el <= l[0]:
        return -1
    if el > l[len(l) - 1]:
        return len(l)
    i = 0
    while i < len(l) and el > l[i]:
        i += 1
    return i
