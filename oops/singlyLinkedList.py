class Node:
    def __init__(self,value):
        self.val = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertatbegining(self,value):
        new_node = Node(value)
        new_node.next = self.head 
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        

    def insertatEnd(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return 
        current = self.head
        while current.next is not None:
            current = current.next
        current.next=new_node    
         
       
insert = SinglyLinkedList()

insert.insertatEnd(2)
insert.insertatEnd(3)
print(insert.print_list())