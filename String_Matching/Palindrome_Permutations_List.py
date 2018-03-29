"""
Given a string s, return all the palindromic permutations (without duplicates) of it. 
Return an empty list if no palindromic permutation could be form.

For example:

Given s = "aabb", return ["abba", "baab"].

Given s = "abc", return []

"""
def find_permutations(input):
    #print(input)
    length = len(input)
    if length==0:
        return []
    elif length==1:
        return [input]
    l = []
    for i in range(length):
        letter = input[i]
        remList = input[:i]+input[i+1:]
        
        for p in find_permutations(remList):
            #print(p)
            l.append(letter+p)
    return l

def is_permutable(input):
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

input = '123'
print(find_permutations(input))