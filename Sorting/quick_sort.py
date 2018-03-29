'''
Created on Mar 15, 2018

@author: kur4ve
'''
def partition(A, low, high):
    last_high = low
    pivot = A[high]
    while low<high:
        if A[low]<pivot:
            #Swap the elements
            A[low], A[last_high] = A[last_high], A[low]
            last_high+=1
        low+=1
    A[high], A[last_high] = A[last_high], A[high]
    return last_high

def quick_sort(A, low, high):
    if low<high:
        pivot = partition(A, low, high)
        quick_sort(A, low, pivot-1)
        quick_sort(A, pivot+1, high)
        
A = [534,246,933, 127,277,321,454,565,220, 230]
print("Given Array ",A)
quick_sort(A, 0, len(A)-1)
print("Sorted Array ",A)