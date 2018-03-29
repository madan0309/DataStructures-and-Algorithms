"""
Subset Sum: Given a sequence of n positive numbers A1 ... A11, give an algorithm which checks
whether there exists a subset of A whose sum of all numbers is T?
return the number of subsets

"""
L = []
def subset(arr, total, i, current_set=[]):
    #print(total, i)
    if total==0: L.append(current_set);
    elif total<0: return 0;
    elif i<0: return 0;
    elif arr[i]>total:
        return subset(arr, total, i-1, current_set)
    else:
        subset(arr, total, i-1, current_set)
        subset(arr, total-arr[i], i-1, current_set+[arr[i]])
    return L

arr = [1,2,3,4,5,1,5,7,3,5,7]
print(len(subset(arr,18 ,len(arr)-1)))