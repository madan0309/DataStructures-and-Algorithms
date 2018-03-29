"""Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n)
to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively."""
def merge_lists(arr1, m, arr2,n):
    p = q = i = 0
    res = []
    while(p<m and q<n):
        if nums1[p]<nums2[q]:
            res[i] = nums1[p]
            p+=1
        else:
            res[i] = nums2[q]
            q+=1
        i+=1
    while(p<m):
        res[i] = nums1[p]
        p+=1
        i+=1

    while(q<n):
        res[i] = nums2[q]
        q+=1
        i+=1
    return res
A = [1,3,4,6]
B = [0,2,5]
print merge_lists(A, 4, B, 3)
