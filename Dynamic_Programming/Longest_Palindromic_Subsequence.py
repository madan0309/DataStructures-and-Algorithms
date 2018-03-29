
d={}
def rec(string, i, j):
    #print(i,j)
    #print(d)
    key = str(i)+'-'+str(j)
    if d.get(key):
        return d[key]
    elif i==j:
        return 1
    elif j-i==1 and string[i]==string[j]:
        return 2
    elif string[i]==string[j]:
        result = 2+rec(string, i+1, j-1)
    else:
        result = max(rec(string, i+1, j), rec(string, i, j-1))
    d[key] = result
    return d[key]

string = '"ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"'
print(rec(string, 0, len(string)-1))
#print(d)