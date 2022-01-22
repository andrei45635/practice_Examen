from merge_sort import *
from binary_sort import *
from divide_impera_nr_neg import *
from dynamic_programming import *

def f(x):
    x += 2
    return x

if __name__ == '__main__':
    array = [5,9,1,3,7,5,6,8,4,1,2,3,6,9,85,2,7]
    merge_sort(array, 0, len(array)-1)
    print(array)
    array_1 = [34, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
    binarySIterative(37, array_1)
    #print(divide(array_1))
    #print(fibbonaci_dumb(12))
    array_2 = [-2,-5,1,2,4,5,6,12,1241,123,-4,-4,2,-1,-5]
    print("Numerele negative sunt:",divide_impera(array_2))
    x = 1
    f(1)
    print(x)