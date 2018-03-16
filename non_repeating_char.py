'''
Created on Mar 12, 2018

@author: kur4ve
'''
def non_repeating(given_string):
    ans = None
    i = 0
    d = {}
    while(i<len(given_string)):
        item = given_string[i]
        if d.get(item)==None:
            d[item] = True
        else:
            d[item] = False
        i+=1
    print given_string, d
    for letter in given_string:
        if d[letter]:
            return letter
    return None

# NOTE: The following input values will be used for testing your solution.
print non_repeating("abcab") # should return 'c'
print non_repeating("abab") # should return None
print non_repeating("aabbbc") # should return 'c'
print non_repeating("aabbdbc") # should return 'd'