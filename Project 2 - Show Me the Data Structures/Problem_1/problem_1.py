# Problem 1: Least Recently Used (LRU) Cache

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache_dic = {}
        self.size = 0
        self.head = None
        self.tail = None

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache_dic:
            node = self.cache_dic[key]
            self.remove_node(node)
            self.set_values(node)
            return node.value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.size == self.capacity:
            self.remove_cache()
        node = Node(value)
        self.cache_dic[key] = node
        self.set_values(node)
        self.size += 1
    
    def set_values(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.next = node
            node.prev = self.head
            if self.head.prev == None:
                self.tail = self.head
            self.head = node
        
    def remove_node(self, node):
        if self.size == 1:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.prev
            self.head.next = None
        elif node == self.tail:
            self.tail.next.prev = None
            self.tail = self.tail.next
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        
    def remove_cache(self):
        node = self.tail
        del self.cache_dic[node.value]
        self.remove_node(node)
        self.size -= 1

        
# Test cases

print("LRU_Cache(5)")
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print("our_cache.get(1): {}".format(our_cache.get(1)))         # returns 1
print("our_cache.get(2): {}".format(our_cache.get(2)))         # returns 2
print("our_cache.get(9): {}".format(our_cache.get(9)))         # returns -1 because 9 is not present in the cache
our_cache.set(5, 5) 
our_cache.set(6, 6)
print("our_cache.get(3): {}".format(our_cache.get(3)))         # returns -1 because the cache reached its capacity and 3 was the least recently used entry

print("\nLRU_Cache(3)")
our_cache = LRU_Cache(3)
our_cache.set(1, 1)
our_cache.set(2, 2)
print("our_cache.get(1): {}".format(our_cache.get(1)))         # returns 1
print("our_cache.get(3): {}".format(our_cache.get(3)))         # returns -1 because 3 is not present in the cache
our_cache.set(3, 3)
print("our_cache.get(3): {}".format(our_cache.get(3)))         # returns 3

print("\nLRU_Cache(1)")
our_cache = LRU_Cache(1)
our_cache.set(1, 1)
print("our_cache.get(1): {}".format(our_cache.get(1)))         # returns 1
print("our_cache.get(2): {}".format(our_cache.get(2)))         # returns -1 because 2 is not present in the cache
our_cache.set(2, 2) 
print("our_cache.get(1): {}".format(our_cache.get(1)))         # returns -1 because 1 is not present in the cache
print("our_cache.get(2): {}".format(our_cache.get(2)))         # returns 2
print("our_cache.get(None): {}".format(our_cache.get(None)))   # returns -1