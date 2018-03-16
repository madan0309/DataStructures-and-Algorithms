'''
Created on Mar 15, 2018

@author: kur4ve
'''
def merge_sort(A):
    #print(A), len(A)/2
    if len(A)>1:
        mid = len(A)//2
        lhalf = A[:mid]
        rhalf = A[mid:]
        
        merge_sort(lhalf)
        merge_sort(rhalf)
        
        i = j = k = 0
        print(lhalf, rhalf)
        while(i<len(lhalf) and j<len(rhalf)):
            if lhalf[i] < rhalf[j]:
                A[k] = lhalf[i]
                i+=1
            else:
                A[k] = rhalf[j]
                j+=1
            k+=1
        #Remaining elements
        while(i<len(lhalf)):
            A[k] = lhalf[i]
            i+=1
            k+=1
            
        while(j<len(rhalf)):
            A[k] = rhalf[j]
            j+=1
            k+=1
            
A = [534,246,933, 127,277,321,454,565,220, 230]
merge_sort(A)
print("Final")
print(A)