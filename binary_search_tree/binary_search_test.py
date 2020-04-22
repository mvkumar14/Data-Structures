from binary_search_tree import BinarySearchTree

test = BinarySearchTree(3)

arr = [1,2,4,5,6,7,8]
for i in arr:
    test.insert(i)

print(test.left.value,test.value,test.right.value)

print(test.contains(4))

print(test.get_max())

test.in_order_print()
