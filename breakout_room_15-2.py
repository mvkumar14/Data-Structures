# Previous_node = None
#     Current_node = sll.head
#     While True:    
#         Move up the list
#         Make a new node pointing the the previous node
#         If you hit the end 
#             break

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def add(self,value):
        self.next = Node(value)

class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = head
    def add(self,value):
        new_node = Node(value)
        self.next = new_node
        

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d
d.next = None

def reverse_sll(node1):
    current_node = node1
    prev_node = None

    while current_node != None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node

for i in [a,b,c,d]:
    if i.next:
        print(i.next.value)
    else: 
        print(None)
reverse_sll(a)
for i in [a,b,c,d]:
    # print(i.next)
    if i.next:
        print(i.next.value)
    else: 
        print(None)