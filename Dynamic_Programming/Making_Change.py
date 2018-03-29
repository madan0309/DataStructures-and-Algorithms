"""

"""
#This is without dynamic programming
def making_coins(coins, i, n):
    print(i, n)
    if n==0:
        return 1
    elif n<0:
        return 0
    elif (i<0 and n>=1):
        return 0
    return making_coins(coins, i-1, n) + making_coins(coins, i, n-coins[i]);

coins = [1,2,3]
n = 4
print(making_coins(coins, len(coins)-1, n))

from collections import defaultdict
d = defaultdict(int)

def dp_making_coins(coins, i, n):
    if d[str(i)+str(n)]:
        return d[str(i)+str(n)]
    elif n==0:
        return 1
    elif n<0:
        return 0
    elif (i<0 and n>=1):
        return 0
    else:
        d[str(i)+str(n)] = dp_making_coins(coins, i-1, n) + dp_making_coins(coins, i, n-coins[i]);
    return d[str(i)+str(n)]
print(dp_making_coins(coins, len(coins)-1, n))