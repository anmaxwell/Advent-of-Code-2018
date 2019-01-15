#%%
class Node:  
    def __init__(self, value):

        self.value = value
        self.next = None
        self.previous = None
        return
    
class DoubleLinkedList:  
    def __init__(self):

        self.head = None
        self.tail = None
        return
    
    def add_node(self, item):

        if isinstance(item, Node):           
            if self.head is None:
                self.head = self.tail = item
            else:
                self.tail.next = item
                self.tail = item
                
            item.previous = self.tail
            item.next = self.head