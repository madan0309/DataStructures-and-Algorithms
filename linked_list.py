'''
Created on Mar 4, 2018

@author: kur4ve
'''
class Node(object):
    def __init__(self, data=None, next_node = None):
        self.data = data
        self.next_node = next_node
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def size(self):
        current = self.head
        count = 0
        while(current!=None):
            count += 1
            current = current.get_next()
        return count
    
    def print_node(self):
        current = self.head
        while current:
            print(current.data)
            current = current.get_next()
            
    def insert(self, data, position):
        k=1
        new_node = Node(data=data)
        current_node = self.head
        #Inserting at first
        if position == 1:
            print(self.head)
            new_node.set_next(self.head)
            self.head = new_node
            print(self.head)
            print(new_node.get_next())
        else:
            #Traversing list until position-1
            while(current_node!=None and k<position-1):
                k+=1;
                previous_node = current_node
                current_node = current_node.get_next()
            if current_node!=None:
                #Inserting at middle
                next_node2 = current_node.get_next()
                current_node.set_next(new_node)
                new_node.set_next(next_node2)
            else:
                #Inserting at last
                previous_node.set_next(new_node)
                
    def delete(self, position):
        if self.head==None:
            print("LL is Empty")
            return
        current_node = self.head
        k=1
        if(position==1):
            current_node = self.head
            self.head = current_node.get_next()
            del current_node
        else:
            #Traversing list until position-1
            while(current_node!=None and k<position-1):
                k+=1;
                previous_node = current_node
                current_node = current_node.get_next()
            if current_node!=None:
                #Deleting at middle
                previous_node.set_next(current_node.get_next())
                del current_node
            else:
                #Deleting at last
                print("Position is Empty")
    def find_node_from_last(self, position):
        current = self.head
        d = {}
        count = 0
        while(current):
            d[count] = current.get_data()
            current = current.get_next()
            count+=1
        print(d)
        return d[count-position+1]
    
    def find_node_from_last2(self, position):
        b_pointer = self.head
        a_pointer = self.head
        for i in range(position):
            b_pointer = b_pointer.get_next()
        while(b_pointer != None):
            b_pointer = b_pointer.get_next()
            a_pointer = a_pointer.get_next()
        return a_pointer.get_data()