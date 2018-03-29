"""
Maximum Value Contiguous Subsequence: Given a sequence of n m1mbcrs 11(1) ...J\(11). 
give a n a lgorithm for finding a contiguous subsequence A(i) .. . A(j) 
for which the s um of clements in the subsequence is maximum. 
Example: {-2, 11, -4, 13, -5, 2} --+ 20 and {l, -3, 4 , -2 , -1, 6}-+ 7.

"""

def kadane_algo(array):
    if len(array)==0:
        return 0
    current_max = global_max = array[0]
    for i in range(1,len(array)):
        current_max = max(array[i], current_max+array[i])
        if current_max>global_max:
            global_max = current_max
    return global_max

input = [-2, 11, -4, 13, -5, 2]
print(kadane_algo(input))

input = [1, -3, 4, -2, -1, 6]
print(kadane_algo(input))

