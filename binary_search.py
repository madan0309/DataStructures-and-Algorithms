'''
Created on Jan 3, 2018

@author: kur4ve
'''
#code
def binary_search(list, target, count):
    end = len(list)
    #print list, target, count, list[(end)//2]
    if end:
        mid = (end)//2-1
        if(list[mid]==target):
            count+=1
            return count
        elif(list[mid]<target):
            count+=1
            return binary_search(list[mid+1:], target, count)
        else:
            count+=1
            return binary_search(list[0:mid], target, count)
    else:
        return 100000000

#list = range(10)
#print(binary_search(list, 8))
N = int(input())
for i in range(N):
    count = 0
    s = raw_input().split()
    #s = [int(r) for r in arr]
    count = binary_search(range(int(s[0])), int(s[1])-1, 0)
    print("count",count)
    gautham = int(s[2])
    subash = int(s[3])
    g_score = gautham*int(s[1])
    s_score = (count-1)*subash
    if(g_score<s_score):
        print(1)
    elif(g_score>s_score):
        print(2)
    else:
        print(0)