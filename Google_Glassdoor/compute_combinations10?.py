"""
Given a string consists of 0,1 and ?, where ? can be 0 or 1 Find all possible combinations of strings.
"""
L = []
input = "10?0?1?11?0?"
def compute(str, i, n):
    if i==n:
        L.append(str)
    else:
        while(i<n and input[i]!='?'):
            str = str + input[i]
            i+=1
        if(i==n):
            L.append(str)
        else:
            compute(str+"0", i+1, n)
            compute(str+"1", i+1, n)
compute("", 0, len(input))
print(L)
print(input.count('?'))
print(len(L))
            