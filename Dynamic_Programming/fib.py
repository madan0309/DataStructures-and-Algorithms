from __future__ import division
"""
Compute fibonacci value at index n

"""

"""This function doesn' use DP so there will be lot of repetitive calculations"""

from collections import defaultdict
import time


def fibonacci(n):
    #print("computing fib of {}".format(n))
    if n==0: return 0;
    elif n==1: return 1;
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print("Without Using Dynamic Programming")
t1 = time.time()
print(fibonacci(30))
t2 = time.time()
r1 = t2-t1
print("Computation time {}".format(t2-t1))

d = defaultdict(int)

def dp_fibonacci(n):
    if d[n]:
        return d[n]
    elif n==0: return 0;
    elif n==1: return 1;
    else:
        d[n] = dp_fibonacci(n-1) + dp_fibonacci(n-2)
        return d[n]
print("\nUsing Dynamic Programming")
t1 = time.time()
print(dp_fibonacci(30))
t2 = time.time()
r2 = t2-t1
print("Computation time {}".format(t2-t1))
#print(d)
print("\nDynamic Programming is {} times faster".format(r1/r2))
