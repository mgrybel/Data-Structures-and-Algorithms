In Problem 1, Least Recently Used (LRU) Cache, a hash map is utilised to store cached values for immediate retrieval of the nodes and values. A doubly linked list (DLL) is used to record the values and the current size. The use of the DLL allows for setting up quickly the head, which represents the most recently used values, and removing the values from the cache. 

get() operation:
- The time complexity of the get() operation is O(1) since this task takes constant time, and there are no loops in the code. 
- The space complexity of the get() operation is O(1) since there is only one allocated variable. 

set() operation:
- The time complexity of the set() operation is O(1) since this task takes constant time, and there are no loops in the code.  
- The space complexity of the set() operation is O(n) because the size of the dictionary is determined by the amount of the keys. 