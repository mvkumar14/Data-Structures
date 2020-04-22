import sys
sys.path.append('G:/Data/Lambda/CS/Data-Structures/doubly_linked_list')
from doubly_linked_list import DoublyLinkedList



class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        # O(1) for both modifying the front and the back
        # doesn't have to exist in contiguous memory
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size += 1
        pass

    def dequeue(self):
        if self.storage.length > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return None

    def len(self):
        return self.size


my_queue = Queue()
queue_2 = my_queue

test = 5
test2 = test
test2 += 1

print(test,test2)
# my_queue.enqueue(1)

# print(my_queue.len())
# print(queue_2.len())
