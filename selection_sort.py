def selectionSort(l):
    """
     sort the element of the list
     l - list of element
     return the ordered list (l[0]<l[1]<...)
     """
    for i in range(0, len(l)-1):
        ind = i
        for j in range(i+1, len(l)):
            if l[j] < l[ind]:
                ind = j
        if i < ind:
            l[i], l[ind] = l[ind], l[i]


if __name__ == '__main__':
    l = [5,9,1,3,7,5,6,8,4,1,2,3,6,9,85,2,7]
    selectionSort(l)
    print(l)