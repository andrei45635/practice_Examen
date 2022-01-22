def directSelectionSort(l):
    """
    sort the element of the list
    l - list of element
    return the ordered list (l[0]<l[1]<...)
    """
    for i in range(0,len(l)-1):
     #select the smallest element
         for j in range(i+1,len(l)):
             if l[j]<l[i]:
                 l[i],l[j] = l[j],l[i]