def bubble_sort(l):
    for i in range(1,len(l)):
        for j in range(len(l) - i):
            if l[j+1] < l[j]:
                l[j], l[j+1] = l[j+1], l[j]

if __name__ == '__main__':
    l = [5,9,1,3,7,5,6,8,4,1,2,3,6,9,85,2,7]
    bubble_sort(l)
    print(l)
