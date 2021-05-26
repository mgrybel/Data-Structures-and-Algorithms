In Problem 5, Blockchain, two classes are utilised: Block and Blockchain. Each of the nodes in the linked list points to the next node, while also storing its current hash and its previous hash values. 

append_block operation:
- The time complexity of the append_block operation is O(1) since the function takes constant time (we only go through a linked list)
- The space complexity of the append_block operation is O(n) because of the space for the linked list and the space for the hash sha. Therefore, we have O(2n), which is then simplified to O(n).