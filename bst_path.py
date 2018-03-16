'''
Created on Jan 15, 2018

@author: kur4ve
'''
import sys
sys.setrecursionlimit(1500)
class Node():
    def __init__(self, data=None, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
        
class BST():
    def insert(self, item, root):
        if root.data:
            if item<=root.data:
                if root.left:
                    self.insert(item, root.left)
                else:
                    new_node = Node(item, parent=root)
                    root.left = new_node
                    nodes[item] = new_node
            else:
                if root.right:
                    self.insert(item, root.right)
                else:
                    new_node = Node(item, parent=root)
                    root.right = new_node
                    nodes[item] = new_node
        else:
            root = Node(item)
        
    def find_path(self, node1, node2):
        path1 = []
        path2 = []
        while(node1.parent != None):
            path1.append(node1.parent.data)
            node1 = node1.parent
        print path1
        
        while(node2.parent != None):
            path2.append(node2.parent.data)
            node2 = node2.parent
        print path2
        common_node = None
        for i in path1:
            if i in path2:
                common_node = i
                break
        print common_node
        final_path = []
        for i in path1:
            final_path.append(i)
            if i == common_node:
                break
            
        for j in path2:
            final_path.append(j)
            if j == common_node:
                break
        #print final_path
        print max(final_path)
    
N = input()
array = map(lambda x:int(x), raw_input().split())
X , Y = map(lambda x:int(x), raw_input().split())
root = Node(array[0])
from collections import defaultdict
nodes = defaultdict()
nodes[array[0]] = root
bst = BST()
for j in range(1,N):
    bst.insert(array[j], root)
#print nodes
bst.find_path(nodes[X], nodes[Y])