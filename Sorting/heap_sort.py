"""
Heap sort- build heap and then print the sorted array
"""
def heapify(arr, i, n):
    l = 2*i+1 #left child
    r = 2*i+2 #right child
    largest = i #assume that root is largest
    
    if l<n and arr[largest]<arr[l]:
        largest = l
    if r<n and arr[largest]<arr[r]:
        largest = r
        
    if largest != i:
        #swap largest element with root
        arr[largest],arr[i] = arr[i], arr[largest]
        #Heapify array at index largest
        heapify(arr, largest, n)
        
def heap_sort(arr):
    n = len(arr)
    print("Array before building into heap {}".format(arr))
    #Building Heap
    for i in range(n-1, -1, -1):
        heapify(arr, i, n)
    print("Array after heapifying {}".format(arr))
    
    #heapsort
    for i in range(n-1, -1, -1):
        #swap max element in array
        arr[0], arr[i] = arr[i], arr[0]
        #heapify the root node
        heapify(arr, 0, i)
    print("Array after sorting {}".format(arr))
A = [534,246,933, 127,277,321,454,565,220, 230]
heap_sort(A)