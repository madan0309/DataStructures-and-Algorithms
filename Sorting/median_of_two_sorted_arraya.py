"""There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n))."""

from __future__ import division
def median(list1, list2):
    n = len(list1)
    #print(list1, list2)
    if n==1:
        return (list1[0]+list2[0])/2
    elif n==2:
        return (max(list1[0], list2[0])+min(list1[1],list2[1]))/2
    mid = int(n//2)
    if n%2==0:
        m1 = (list1[mid]+list1[mid-1])/2
        m2 = (list2[mid]+list2[mid-1])/2
    else:
        m1 = list1[mid]
        m2 = list2[mid]
    #print(list1, list2, m1, m2)
    if m1==m2:
        return m1
    elif m1>m2:
        if n%2==0:
            return median(list1[:mid], list2[mid:])
        else:
            return median(list1[:mid+1], list2[mid:])
    else:
        if n%2==0:
            return median(list1[mid:], list2[:mid])
        else:
            return median(list1[mid:], list2[:mid+1])
    
list1 = [1,2,3,4,5,6]
list2 = [3,6,6,7,8,9]
print(median(list1, list2))