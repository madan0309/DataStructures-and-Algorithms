"""
Given two str;ngs: string X of length m [X(l..m)], and string Y of length 11 [Y(l..n)I, 
find the longest common subsequence: 
the longest sequence of characters that appear left-to-right (but not necessarily in a contiguous block)

X = 'ABCB'
Y = 'RBDCBE'
ans = 3 BCB
"""
import time
"""Without using dynamic programming"""
def lcs(X, Y, n, m):
    if (n==0 or m==0): return 0;
    elif X[n-1]==Y[m-1]:
        return 1+lcs(X, Y, n-1, m-1)
    else:
        temp1 = lcs(X, Y, n-1, m)
        temp2 = lcs(X, Y, n, m-1)
        result = max(temp1, temp2)
    return result
X = "ABCBDABABCBDCBDABDABBBCBDAB"
Y = "BDCABAABCBDABABABDAB"
print("Without Using Dynamic Programming")
t1 = time.time()
print(lcs(X, Y, len(X), len(Y)))
t2 = time.time()
r1 = t2-t1
print("Computation time {}".format(t2-t1))

"""Using Dynamic Programming"""
n = len(X)
m = len(Y)
d = [[None]*m for i in range(n)]
def dp_lcs(X, Y, n, m):
    if n==0 or m==0: return 0
    elif d[n-1][m-1]:
        return d[n-1][m-1]
    elif X[n-1]==Y[m-1]: return 1+dp_lcs(X, Y, n-1, m-1)
    else:
        temp1 = dp_lcs(X, Y, n-1, m)
        temp2 = dp_lcs(X, Y, n, m-1)
        result = max(temp1, temp2)
    d[n-1][m-1] = result
    return d[n-1][m-1]
print("\nUsing Dynamic Programming")
t1 = time.time()
print(dp_lcs(X, Y, n, m))
t2 = time.time()
r2 = t2-t1
print("Computation time {}".format(t2-t1))
print("\nDynamic Programming is {} times faster".format(r1/r2))