# from dll_stack import Stack
# from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')
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
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return
        else:
            value = node.value
            self.delete(node)
            self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.tail:
            return
        else:
            value = node.value
            self.delete(node)
            self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # TODO: Catch errors if list is empty or node is not in list
        # for now assuming node is in list
        self.length -= 1
        # if head and tail
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # if head
        elif node is self.head:
            self.head = self.head.next  # or node.next
            node.delete()
        # if tail
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            # if regular node
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        # Loop through all nodes, looking for biggest value
        # TODO: Error checking
        if not self.head:
            return None
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # * we can see what comes before and after in the queue with a doubly linked list
        self.storage = DoublyLinkedList()

    def push(self, value):
        # in a stack as things get added they get added to the end of the list
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        # check to see if there is anything to remove
        # when removing something from a stack you have to move the item on top of the stack (the most recently added item)
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return None

    def len(self):
        return self.size
class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # * we can see what comes before and after in the queue with a doubly linked list
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # when adding something to a queue you add it to the end of the line
        # so you would need to add it to the tail of the list
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        # when removing something from a queue you remove it from the beginning of the line 
        # check to see if there is something to dequeue
        if self.size > 0:
        #if there is decrease the size by 1 and remove from queue
            self.size -= 1
            return self.storage.remove_from_head()
        # otherwise there is nothing in the queue so there is nothing to return (excpet None)
        else:
            return None

    def len(self):
        return self.size

'''
insert:
    recursion
    #* base case
    check if empty
    if empty
        put node here/at root
    else:
        if new < node.value
            leftnode.insertvalue
        if new >= node.value
            rightnode.insertvalue

get_max:
    max is always going to be the right most node
    if theres a right:
        get max on right
    else:
        return node.value

find:
    #* base case
    if node is None:
        return False 
    if node.value == findvalue:
        return True
    else:
        if findvalue < node.value:
            find on left node
        else:
            find on right node
for_each:
    if node is None:
        return Null
    else:
        if node.right:
            node.right.foreach(cb)
        if node.left:
            node.left.foreach(cb)
'''

#* Remember every node is a (BinarySearchTree) with left and right values
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #* base case
        # check if empty
        if self.value == None:
            #if it is put node here
            self.value == value
            print(f"value {self.value}")
        else:
            #if it's not empty and smaller than node put new node to the left
            if value < self.value:
                # check if there is anything on left
                if self.left != None:
                    #if there is then go left again
                    self.left.insert(value)
                else:
                    #if there isn't, insert node here
                    self.left = BinarySearchTree(value)
            #if it's not empty and larger than node put new node to the right
            if value >= self.value:
                #check if there's anything to the right:
                if self.right != None:
                    # if there is go right again 
                    self.right.insert(value)
                else:
                    #if there isn't, insert node here
                    self.right = BinarySearchTree(value)
    def contains(self, target):
        # base case
        #if there is no value return false
        if self.value == None:
            return False
        #if self.value is equal to the target return true
        if self.value == target:
            return True
        else:
            #if the target is less than self.value and there is a self.left check the left
            if target < self.value and self.left:
                return self.left.contains(target)
            # if the target is larger than self.value and there is a self.right check the right
            elif target > self.value and self.right:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # max number will always be to the right
        #if there is a right. get max on right
        if self.right != None:
            return self.right.get_max()
        # if there isn't a right, that is the max value
        else:
            #return max value
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #base case
        # if there is no value there is nothing you can do
        #* ended up not needing the below check 
        # if self.value == None:
        #     pass
        # else:
        
        # if there is a value
        if self.value:
            # perform the cb fn on that value
            cb(self.value)
        # if there is a right value
        if self.right != None:
            # recurse to use the cb fn on that value and keep going right until you cant
            self.right.for_each(cb)
        # if there is a left value
        if self.left != None:
            # recurse to use the cb fn on that value and keep going left until you cant
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
