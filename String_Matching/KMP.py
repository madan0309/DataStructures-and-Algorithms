def prefix_table(pattern):
    m = len(pattern)
    k = 0
    F = [0]*m
    print(list(pattern))
    for i in range(1, m):
        print(F, i, k)
        while(k>0 and pattern[i]!=pattern[k]):
            print(k, F[k-1])
            k = F[k-1]
        if pattern[i]==pattern[k]:
            k += 1
        F[i] = k
    return F

def kmp_match(text, pattern):
    prefix_talbe = prefix_table(pattern)
    print("Final Prefix Table: ", prefix_talbe)
    k = 0
    n = len(text)
    m = len(pattern)
    L = []
    for i in range(n):
        while(k>0 and pattern[k]!=text[i]):
            k = prefix_talbe[k-1]
        if pattern[k]==text[i]:
            k+=1
        if k==m:
            L.append(i-m+1)
            k = 0
    return L
text = "abcdababacafacdbabcabababaca"
input = "ababaca"
print(kmp_match(text, input))