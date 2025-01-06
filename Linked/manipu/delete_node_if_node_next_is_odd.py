'''
delete node if next is odd
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Lined_list:
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
        current = self.head
        while current:
            print(current.data,end=" ")
            current = current.next
        print()
            
    def delete(self):
        current = self.head
        prev = None
        
        while current:
            if current.next and current.next.data % 2 == 1:
                # print(current.next.data)
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
                
    def delete_next(self):
        current = self.head
        prev = None
        
        while current:
            if current.next and current.next.next and current.next.next.data % 2 == 1:
                # print(current.next.data)
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
                
                
List = Lined_list()
List.append(1)
List.append(2)
List.append(3)
List.append(4)
List.append(5)
List.append(6)
List.append(7)
List.append(8)
List.display()
# List.delete()
# List.display()
List.delete_next()
List.display()