"""

"""
from collections import defaultdict
d = defaultdict(int)

def dp_making_coins(coins, i, n):
    print(i,n)
    if d[str(i)+str(n)]:
        return d[str(i)+str(n)]
    elif n==0:
        return 1
    elif n<0:
        return 1000000000
    elif (i<0 and n>=1):
        return 1000000000
    else:
        temp1 = dp_making_coins(coins, i-1, n)
        temp2 = 1+dp_making_coins(coins, i, n-coins[i])
        d[str(i)+str(n)] = min(temp1, temp2);
    return d[str(i)+str(n)]

coins = [1,5,10,20,25,50]
n = 40
print(dp_making_coins(coins, len(coins)-1, n))