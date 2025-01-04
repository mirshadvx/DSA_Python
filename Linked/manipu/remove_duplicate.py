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
    
    def get_list_len(self):
        current_node = self.head
        count = 0
        
        while current_node:
            current_node = current_node.next
            count += 1
            
    def delete_duplicate(self):
        seen = set()
        current = self.head
        prev_node = None
        
        while current:
            if current.data in seen:
                prev_node.next = current.next
                if current == self.tail:
                    self.tail = current
            else:
                seen.add(current.data)
                prev_node = current
            
            current = current.next
            

List = Linked_List()
List.append(100)
List.append(1)
List.append(2)
List.append(3)
List.append(2)
List.append(10)
List.append(80)
List.append(100) 

print("Original List:")
List.display()

List.delete_duplicate()

print("List after removing duplicates:")
List.display()
