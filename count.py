'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
import re
# Write your code here
def compute_string(str):
    d = {}
    #L = list(str)
    L = re.findall(r"([a-z])([0-9]+)",str)
    for i in L:
        if i[0] not in d:
            d[i[0]] = int(i[1])
        else:
            d[i[0]]+= int(i[1])
    return d


s = raw_input()
final_s = compute_string(s)
sorted_keys = sorted(final_s.keys())
Q = input()
l = sum(final_s.values())
for i in range(0,Q):
    r = input()
    if r>l:
        print -1
    else:
        for i in sorted_keys:
            r = r-final_s[i]
            if r<=0:
                print i
                break