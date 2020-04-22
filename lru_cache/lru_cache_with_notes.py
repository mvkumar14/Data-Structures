import sys
sys.path.append('G:/Data/Lambda/CS/Data-Structures/doubly_linked_list')

from doubly_linked_list import DoublyLinkedList, ListNode

# Right now I delete objects from the dictionary ineffectivley
# another way to do it would be to keep track of lru_key 
# and constantly update it when other operations occur? 
# there are some edge cases to work out for that implimentation. 


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.lookup = {}
        self.storage = DoublyLinkedList()
        # need to track
        # maximum number of nodes it can hold
        # current number of nodes it is holding
        # a dll that stores the entries
        # a dictionary that maps keys to pointers to 
        # dll nodes to access the nodes in the cache.
        # when you add an item to the list you have to provide
        # a key so that you can access that item speicifically later
        # the key is looked up in a dictionary and its matching value
        # should be a pointer to the node in the dll.
        pass

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.lookup:
            if self.lookup[key].value != None:
                self.recently_used(key)
                return self.lookup[key].value
            else: # if self.lookup[key] exists, and the object's value is none
                del self.lookup[key]
                # delete the key from the dict
                return None
        else:
            return None
        # check if the key is valid
        # if the key isn't valid (points to none )
            # return None
        # else: (if the key is valid)
            # do the "priority dance"
            # return node's value
            # self.dict[key].value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.lookup:
            self.lookup[key].value = value
            self.recently_used(key)
        else:
            self.size += 1
            self.storage.add_to_head(value)
            self.lookup[key] = self.storage.head
            if self.size > self.limit:
                self.remove_last()
        # if key exists:
            # change value of key
            # priority dance
        # else (make new key)
            # add key to beginning of dll
            # remove_if necessary

    def recently_used(self,key):
        # assume checking the key has already been done:
        update_node = self.lookup[key]
        self.storage.move_to_front(update_node)
        pass
        # this is the "priority_dance"
        # this function has to be called when any
        # updates occur. It isn't called when a new 
        # key value is added because it automatically 
        # gets added to the front of the dll.
        
        # move the key node to the front of the dll
    
    def remove_key(self,key):
        del self.lookup[key]
        pass # is this needed?

    def remove_last(self):
        # assuming checking of keys has already been done

        # the next 5 lines deletes the key from the dictionary
        # I don't keep track of the key 
        # this probably doesn't scale well because it is a list
        # traversal (through .index()) every time you want to delete
        # something.

        # This takes advantage of ordering to find the key (I want to remove that
        # for more general purpose usage (outside of python that offers this feature))
        # obj_to_delete = self.storage.tail
        # my_dict = self.lookup
        # key_index = list(my_dict.values()).index(obj_to_delete)
        # key_to_delete = list(my_dict.keys())[key_index]
        # del self.lookup[key_to_delete]

        # Set the value of the node to none, and then later
        # when you access the dictionary again handle the case where
        # the value of the node that the dictionary points to is none
        self.storage.tail.value = None

        self.storage.remove_from_tail()
        pass
        # if the length is greater than capacity
            # remove the last thing in the dll
        # else:
            # pass
