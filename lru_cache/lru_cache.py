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

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

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

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    def move_to_front(self, node):
        if node is self.head:
            return
        else:
            value = node.value
            self.delete(node)
            self.add_to_head(value)

    def move_to_end(self, node):
        if node is self.tail:
            return
        else:
            value = node.value
            self.delete(node)
            self.add_to_tail(value)

    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = self.head.next
            node.delete()
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()

    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    #* keeps track of:
                #* Limit
                #* current_nodes_len(size)
                #* DLL(holds key value pairsin correct order)
                #* storage dict
    """

    def __init__(self, limit=10):
        # limit
        self.limit = limit
        # current number of nodes
        self.size = 0
        # DLL that holds order of key:value in correct order
        self.dll = DoublyLinkedList()
        # A dict for storage and easy access
        self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    #* retrieve the value associated with given key
    #* move that key:value pair to the end of the order
    #* Return the value associated with given key
    #* Return none if key:value pair is not in cache
    """

    def get(self, key):
        # If key:value pair does not exist return None
        if key not in self.cache:
            return None
        # retrieve the value associated with given key
        else:
            node = self.cache[key]
            # move that key:value pair to the end of the order (most recently used)
            self.dll.move_to_end(node)
            print(f"node {node.value}")
            return node.value[1]
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    #* adds given Key:value pair to cache (self.cache)
    #* if cache is full remove oldest key:value pair and then add new key:value pair
    #* newly added key:value pair should be moved to the end (most recently used) 
    #* if key already exists overwrite old value with new value
    """

    def set(self, key, value):
          # if key already exists overwrite old value with new value
        if key in self.cache:
            node = self.cache[key]
            node.value = (key, value)
            # move to the end to make it the most recently used
            self.dll.move_to_end(node)
        # if cache is full remove oldest key:value pair and then add new key:value pair
        elif self.size == self.limit:
            # remove oldest key:value pair from storage and cache
            del self.cache[self.dll.head.value[0]]
            self.dll.remove_from_head()
            # reduce size to be able to add new key:value
            self.size -= 1
        # add new key:value pair and move to tail
        self.dll.add_to_tail((key, value))
        self.cache[key] = self.dll.tail
        self.size += 1
