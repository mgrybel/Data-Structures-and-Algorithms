In Problem 6, Union and Intersection, the set() function is used to ensure that the union and intersection of two given linked lists do not contain duplicated values. 

union operation:

- The time complexity of the union operation is O(n) because the union utilises two while loops (one for each linked list), and one for loop to iterate through the final set of values. Therefore, we have O(3n), which is then simplified to O(n).
- The space complexity of the union operation is O(n) since each of the linked lists (linked_list_1 and linked_list_2) is allocated to a new variable.

intersection operation:
- The time complexity of the intersection operation is O(n^2) because the intersection utilises a while loop within a while loop to check for identical values in each of the two given linked lists. There is also one for loop to iterate through the final set of values, that is O(n). Therefore, we have O(n^2) + O(n), which is then simplified to O(n^2).
- The space complexity of the intersection operation is O(n) since each of the linked lists (linked_list_1 and linked_list_2) is allocated to a new variable.