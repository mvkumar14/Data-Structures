# Count = 0
# While True:
# Count += 1

# If length/2  != old middle
#     Update the middle
#     New_middle = old_middle.next
#     If same
#         Continue
#     If current_node.next == None:
#         break

import sys
sys.path.append('G:/Data/Lambda/CS/Data-Structures/doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

test_list = DoublyLinkedList()

a = [1,34,54,3,4,6,5,3,2]
for i in a:
    test_list.add_to_tail(i)

def find_middle(sll):
    count = 0
    current_node = sll.head # maybe we can't use head ? come back and check.
    middle_value = current_node.value
    middle_node = current_node
    middle_position = 0
    # todo edge case for length of 1 
    while True:
        current_node = current_node.next
        count += 1
        new_middle = count//2

        if new_middle != middle_position:
            middle_position = new_middle
            middle_value = middle_node.next.value
            middle_node = middle_node.next
            # change middle position
            # change middle value
        
        if current_node.next == None:
            break
    return middle_value


print(find_middle(test_list))

