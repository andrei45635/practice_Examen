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

if __name__ == '__main__':
    array = [5, 9, 1, 3, 7, 5, 6, 8, 4, 1, 2, 14,3, 6, 9, 85, 2, 7,15]
    print(searchSeqOrdered(14, array))