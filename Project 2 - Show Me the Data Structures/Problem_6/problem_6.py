# Problem 6: Union and Intersection

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current_head = self.head
        output_string = ""
        while current_head:
            output_string += str(current_head.value) + "->"
            current_head = current_head.next
        return output_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

def union(linked_list_1, linked_list_2):
    union = LinkedList()
    new_set = set()
    node_1 = linked_list_1.head
    node_2 = linked_list_2.head
    while node_1:
        new_set.add(node_1.value)
        node_1 = node_1.next
    while node_2:
        new_set.add(node_2.value)
        node_2 = node_2.next
    for item in new_set:
        union.append(item)
    return union

def intersection(linked_list_1, linked_list_2):
    intersection = LinkedList()
    new_set = set()
    node_1 = linked_list_1.head
    node_2 = linked_list_2.head

    while node_1:
        while node_2:
            if node_1.value == node_2.value:
                new_set.add(node_1.value)
            node_2 = node_2.next
        node_1 = node_1.next
        node_2 = linked_list_2.head
    for item in new_set:
        intersection.append(item)
    return intersection


# Test Cases

print('----- Test Case 1 -----')
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("--- Linked List 1 ---")
print(linked_list_1) # prints 3->2->4->35->6->65->6->4->3->21->
print("--- Linked List 2 ---")
print(linked_list_2) # prints 6->32->4->9->6->1->11->21->1->
print("--- Union ---")
print (union(linked_list_1,linked_list_2)) # prints 32->65->2->35->3->4->6->1->9->11->21->
print("--- Intersection ---")
print (intersection(linked_list_1,linked_list_2)) # prints 4->21->6->


print('\n----- Test Case 2 -----')
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_3 = [3,2,4,35,6,65,6,4,3,23]
element_4 = [1,7,8,9,11,21,1]

for i in element_3:
    linked_list_3.append(i)

for i in element_4:
    linked_list_4.append(i)

print("--- Linked List 3 ---")
print(linked_list_3) # prints 3->2->4->35->6->65->6->4->3->23->
print("--- Linked List 4 ---")
print(linked_list_4) # prints 1->7->8->9->11->21->1->
print("--- Union ---")
print (union(linked_list_3,linked_list_4)) # prints 65->2->35->3->4->6->1->7->8->9->11->21->23->
print("--- Intersection ---")
print (intersection(linked_list_3,linked_list_4)) # prints nothing


print('\n----- Test Case 3 -----')
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = [1,5,7,23,56,12,9,4,33]
element_6 = []

for i in element_5:
    linked_list_5.append(i)

for i in element_6:
    linked_list_6.append(i)

print("--- Linked List 5 ---")
print(linked_list_5) # prints 1->5->7->23->56->12->9->4->33->
print("--- Linked List 6 ---")
print(linked_list_6) # prints nothing (the linked list is empty)
print("--- Union ---")
print (union(linked_list_5,linked_list_6)) # prints 1->33->4->5->7->9->12->23->56->
print("--- Intersection ---")
print (intersection(linked_list_5,linked_list_6)) # prints nothing


print('\n----- Test Case 4 -----')
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_7 = [1,1,1,1,1,1,1,1,1]
element_8 = [1,1,1,1,1,1,1,1,1]

for i in element_7:
    linked_list_7.append(i)

for i in element_8:
    linked_list_8.append(i)

print("--- Linked List 7 ---")
print(linked_list_7) # prints 1->1->1->1->1->1->1->1->1->
print("--- Linked List 8 ---")
print(linked_list_8) # prints 1->1->1->1->1->1->1->1->1->
print("--- Union ---")
print (union(linked_list_7,linked_list_8)) # prints 1->
print("--- Intersection ---")
print (intersection(linked_list_7,linked_list_8)) # prints 1->