"""
STRING MATCHING
For simplicity, Jet's assume lhat the characters used in string T arc only integers. 
That means, all characters in TE {O,1,2,...,9}. 
Since all of them arc integers, we can view a string of m consecutive characters as decimal numbers.

TEXT = "16828417461893246819491212211"
PATTERN = "8284174"
"""
def hash(pattern):
    hash_value = 0
    i = 0
    while(i<len(pattern)):
        hash_value += ord(pattern[i])
        i+=1
    return hash_value
        
def robin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    pattern_hash = hash(pattern)
    current_hash = hash(text[0:m])
    L = []
    for i in range(n-m+1):
        if current_hash==pattern_hash:
            if text[i:i+m]==pattern:
                L.append(i)
        if(i!= (n-m)):
            current_hash -=  ord(text[i])
            current_hash += ord(text[i+m])
    return L

text = "abcdababacafacdbabcabababaca"
pattern = "ababaca"
print(robin_karp(text, pattern))