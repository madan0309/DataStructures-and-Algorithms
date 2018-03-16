'''
Created on Jan 15, 2018

@author: kur4ve
'''
class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def insert(self, item, root):
        #print root, root.data
        if root.data:
            if (item > root.data):
                if root.right:
                    self.insert(item, root.right)
                else:
                    root.right = Node(item)
            else:
                if root.left:
                    self.insert(item, root.left)
                else:
                    root.left = Node(item)
        else:
            root.data = item
            
    def pre_order(self, root):
        #This will prints the data in Root Left and Right order
        print int(root.data.strip())
        if root.left:
            self.pre_order(root.left)
        if root.right:
            self.pre_order(root.right)
    
    def find_node(self, data, root):
        #print root, root.data, data
        if root.data == data:
            return root
        elif data>root.data:
            #print "searching on right ", root.data, root.right
            return self.find_node(data, root.right)
        elif data<root.data:
            #print "searching on left ", root.data, root.left
            return self.find_node(data, root.left)
N = input()
items = raw_input().split()
#print items
root = Node(items[0])
#print root, root.data
bst = BST()
Q = raw_input()
nodes = [root]
for j in range(1, N):
    bst.insert(items[j], root)
#print bst.find_node('1', nodes[0])
bst.pre_order(bst.find_node(Q, nodes[0]))