"""
Integer Knapsack Problem [Duplicate Items Permitted): Given n types of items, where the iu' 
item type has an integer size s1 and a value v1, We need lo fill a knapsack of total capacity 
C with items of maximum value, We can add multiple items of the same type Lo the knapsack.
"""
values = [60, 100, 120]
caps = [10, 20, 30]

def KS(n, c):
    print(n, c)
    if n==0 or c==0:
        return 0
    elif caps[n]>c:
        return KS(n-1, c)
    else:
        temp1 = KS(n-1, c-caps[n]) + values[n]
        temp2 = KS(n-1, c)
        result =  max(temp1, temp2)
    return result

print(KS(len(caps)-1, 50))