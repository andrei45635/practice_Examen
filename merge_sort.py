def merge(l, left, right, m):
    # Make copies of both ls we're trying to merge

    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = l[left:m+1]
    right_copy = l[m+1:right+1]

    # Initial values for variables that we use to keep
    # track of where we are in each l
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            l[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # Opposite from above
        else:
            l[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while left_copy_index < len(left_copy):
        l[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        l[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


def merge_sort(l,start,end):
    """
     sort the element of the list
     l - list of element
     return the ordered list (l[0]<l[1]<...)
     """
    if start >= end:
        return
    m = (end+start) // 2
    merge_sort(l,start,m)
    merge_sort(l,m+1,end)
    merge(l,start,end,m)