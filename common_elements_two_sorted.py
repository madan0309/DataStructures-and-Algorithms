'''
Created on Mar 12, 2018

@author: kur4ve
'''
def common_elements(list1, list2):
    result = []
    l1 = len(list1)
    l2 = len(list2)
    i = j = 0
    while(i<l1 and j<l2):
        item1 = list1[i]
        item2 = list2[j]
        if item1 == item2:
            result.append(item1)
            i+=1
            j+=1
        elif item1>item2:
            j+=1
        else:
            i+=1
    return result
if __name__ == '__main__':
    list_b1 = [0, 1, 2, 3, 4, 5]
    list_b2 = [6, 7, 8, 9, 10, 11]
    print common_elements(list_b1, list_b2)