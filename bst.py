'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import sys
sys.setrecursionlimit(1500)
class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
class BST():
    def insert(self, item, root):
        if root.data:
            if item<=root.data:
                if root.left:
                    self.insert(item, root.left)
                else:
                    root.left = Node(item)
            else:
                if root.right:
                    self.insert(item, root.right)
                else:
                    root.right = Node(item)
        else:
            root = Node(item)
        
    def height(self, root):
        if root:
            lheight = 1+self.height(root.left)
            rheight = 1+self.height(root.right)
            maximum = max(lheight, rheight)
            return maximum
        return 0
N = input()
array = raw_input().split()
root = Node(array[0])
bst = BST()
for j in range(1,N):
    bst.insert(array[j], root)
print bst.height(root)