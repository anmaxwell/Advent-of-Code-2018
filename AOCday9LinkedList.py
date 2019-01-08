#%%

class Node:  
    def __init__(self, value):
        "constructor class to initiate this object"

        self.value = value
        self.next = None
        self.previous = None
        return

class DoubleLinkedList:  
    def __init__(self):
        "constructor to initiate this object"

        self.head = None
        self.tail = None
        return


    def add_node(self, item, current_marble=None):
        "add an item"

        if isinstance(item, Node):
            if self.head is None:
                self.head = item
                self.tail = item
                item.previous = self.tail
                item.next = self.tail


            else:
                current_marble.next.next.previous = item
                item.previous = current_marble.next
                item.next = current_marble.next.next
                current_marble.next.next = item
                
        current_marble = item

        return(current_marble)
        
    def reset_curmar(self, current_marble):
        current_marble = current_marble.previous.previous.previous.previous.previous.previous.previous
        
        return current_marble

    def remove_node(self, current_marble):
        "remove an item"

        current_marble = current_marble.next
        

def marbleGame(noElves, noMarbles):
        
    game_on = DoubleLinkedList()
    curmar = None
    scores = {}
    noElves = 9
    j=0
    
    for i in range(noMarbles):
        newnode = Node(i)
        
        if i%23 == 0 and i>0:

            if j in scores:         
                scores[j]+=i
            else:
                scores[j]=i
                
            curmar = game_on.reset_curmar(curmar)
            print(curmar.value)
            scores[j]+= curmar.value
            
        else:

            curmar = game_on.add_node(newnode, curmar)     
            
            
        if j ==noElves:
            j=1
        else:
            j+=1
            
    print(max(zip(scores.values(), scores.keys())))
    
marbleGame(9, 25)
        