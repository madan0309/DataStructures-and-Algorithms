#!/bin/python

import sys
from collections import defaultdict
fact_dict = defaultdict()
def initialize(s):
    # This function is called once before all queries.
    pass
    
def fact(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    fact_dict[n] = ans
    return ans

def answerQuery(l, r):
    # Return the answer for this query modulo 1000000007.
    sub_string = s[l-1:r]
    #print sub_string
    d = defaultdict(int)
    for letter in sub_string:
        d[letter]+=1
    #print d
    count_odd = 0; result = 0
    denominator = 1
    r = 0
    for key in d:
        if d[key]/2 in fact_dict:
            denominator = denominator*fact_dict[d[key]/2]
        else:
            denominator = denominator*fact(d[key]/2)
        if d[key]%2 !=0:
            count_odd += 1
        r += d[key]/2
        #if d[key]%2 == 0:
        #    denominator = denominator*fact(d[key]/2)
        #else:
        #    count_odd += 1
    #r = count_even_half = (len(sub_string)-count_odd)/2
    #print 'r',r
    #print 'fact', fact(r)
    if r in fact_dict:
        permutations = fact_dict[r]/denominator
    else:
        permutations = fact(r)/denominator
    if(count_odd):
        result = count_odd*(permutations)
    else:
        result = permutations
    result = result % (10**9+7)
    return result
    
if __name__ == "__main__":
    s = raw_input().strip()
    initialize(s)
    q = int(raw_input().strip())
    for a0 in xrange(q):
        l, r = raw_input().strip().split(' ')
        l, r = [int(l), int(r)]
        result = answerQuery(l, r)
        print result