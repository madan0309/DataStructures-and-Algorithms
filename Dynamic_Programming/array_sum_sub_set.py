'''
Created on Mar 10, 2018

@author: kur4ve
'''
def dp(arr, total, i):
    if total==0:
        return 1
    elif total<0:
        return 0
    elif i<0:
        return 0
    elif total<arr[i]:
        to_return = dp(arr, total, i-1)
    else:
        to_return = dp(arr, total-arr[i], i-1) + dp(arr, total, i-1)
    return to_return

def trigger(arr, total):
    return dp(arr, total, len(arr)-1)


def dp_mem(arr, total, i, mem):
    key = str(total)+":"+str(i)
    if key in mem:
        return mem[key]
    if total==0:
        return 1
    elif total<0:
        return 0
    elif i<0:
        return 0
    elif total<arr[i]:
        to_return = dp_mem(arr, total, i-1, mem)
    else:
        to_return = dp_mem(arr, total-arr[i], i-1, mem) + dp_mem(arr, total, i-1, mem)
    mem[key] = to_return
    return to_return

def trigger_mem(arr, total):
    mem = {}
    return dp_mem(arr, total, len(arr)-1, mem)
import time
s = raw_input()
array = [int(element) for element in s.split()]
print array
sum = input()
t1 = time.time()
print trigger(array, sum)
t2 = time.time()
print "time without dynamic programming :",t2-t1

t3 = time.time()
t4 = time.time()
print trigger_mem(array, sum)
print "time with dynamic programming :",t4-t3


