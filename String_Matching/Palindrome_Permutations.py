"""
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
"""
from collections import defaultdict
def palindrome_permutation(input):
    d = defaultdict(int)
    for letter in input:
        d[letter]+=1
    flag = False
    for letter, count in d.items():
        if count%2!=0 and not flag:
            flag = True
        elif count%2!=0:
            return False
    return True
text = "carerac"
print(palindrome_permutation(text))