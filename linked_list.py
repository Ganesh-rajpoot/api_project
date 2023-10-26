class Node:
    def __init__(self,value) -> None:
        self.data = value
        self.next = None
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    
    def size_of_ll(self):
        return self.size
    def insert_head(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def traverse(self) -> None:
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next
            # return curr.data


l = LinkedList()

a = Node(10)
b = Node(20)
c = Node(30)

# print(a,b,c)
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
print("traverse",l.traverse())



