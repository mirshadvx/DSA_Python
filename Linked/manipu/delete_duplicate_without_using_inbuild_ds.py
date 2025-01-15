class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data,end=' ')
            current_node = current_node.next
        
    def delete_duplicate(self):
        current = self.head
        
        while current:
            prev = current  
            checker = current.next
            
            while checker:
                if checker.data == current.data:
                    prev.next = checker.next
                else:
                    prev = checker
                checker = checker.next
            
            current = current.next
    
        
            
List = Linked_List()
List.append(100)
List.append(1)
List.append(2)
List.append(3)
List.append(1)
List.append(3)
List.append(10)
List.append(80)
List.append(100)
List.display()
print()
List.delete_duplicate()
List.display()