"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # cases
        # list is empty
            # head and tail set to new node
        # list has 1 + elements
        self.length += 1
        new_node = ListNode(value)
        if self.length == 1:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        # create new node
        # set the next pointer to the current head
        # set current head's previous pointer to the new node
        # increase length by one
        pass

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
        # What happens to the dangling head object?

        # delete current node (make sure that delete
        # handles deleting from the front of the list properly)
        # decrease the length by 1
        

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # cases
        # there are no nodes
        # there is one + node(s)
        self.length += 1
        new_node = ListNode(value)
        if self.length == 1: # no nodes previously
            self.head = new_node
            self.tail = new_node
        else: # 2 + nodes
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        pass
        # create new node with value = value
        # set previous value of the new node to the old tail
        # set next value of the new node to None
        # set the next value of the old tail to the new node
        # set the new tail to be the new node
        # increment the length.
        

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
        # make the current tail's previous node 
        # the new tail
        # delete the old tail node
        # decrement length

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if self.head is node:
            return
        self.delete(node)
        self.length += 1
        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if self.tail is node:
            return
        self.delete(node)
        # that delete decreased length
        # so increase it again
        self.length += 1
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node
        pass
        
        # delete node
        # current tail's next = node
        # current node's previous = old tail
        # current nodes's next = None
        # set tail to current node (input node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # Todo: do we need error check if node is not in list? (what list)
        # cases:
        # this is the only node
        # its the head
        # its the tail
        # its in the middle
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        current_node = self.head
        max_value = self.head.value
        while True: # run until break
            if current_node.value > max_value:
                max_value = current_node.value
            if current_node.next: # if the next value isn't none
                current_node = current_node.next
            else: # if the value is none
                break
        return max_value