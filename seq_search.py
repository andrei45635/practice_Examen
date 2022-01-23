#cheile nu sunt ordonate
def searchSeq(el, l):
    """
     Search for an element in a list
     el - element
     l - list of elements
     return the position of the element or -1 if the element is not in l
     """
    poz = -1
    for i in range(len(l)):
        if el == l[i]:
            poz = i
    return poz


#chei ordonate
def searchSeqOrdered(el, l):
    """
     Search for an element in a list
     el - element
     l - list of ordered elements
     return the position of first occurrence or the position where the element can be inserted
     """
    if len(l) == 0:
        return 0
    poz = -1
    for i in range(0, len(l)):
        if el == l[i]:
            poz = i
    if poz == -1:
        return len(l)
    return poz