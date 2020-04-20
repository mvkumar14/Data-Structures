import sys
sys.path.append('G:/Data/Lambda/CS/Data-Structures/doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
        # add to the end
        # increase size
        pass

    def pop(self):
        if self.len() > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return None
        # if not empty
        # remove the last thing added
        # decrease size 
        # if it is empty :
            # return none
            # don't change the size
        pass

    def len(self):
        return self.size
