# Problem 5: Blockchain

import hashlib
import time


class Block:
    
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.data).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class Blockchain:

    def __init__(self):
        self.head = None
        self.size = 0

    def append_block(self, value):
        if value is None:
            return

        node = self.head
        self.size += 1

        if node is None:
            block = Block(time.gmtime(), value, None)
            self.head = block
        else:
            while node.next:
                node = node.next
            node.next = Block(time.gmtime(), value, node.hash)


# Test Cases

print('----- Test Case 1 -----')
blockchain = Blockchain()
blockchain.append_block('Block 0')
print(blockchain.head.data) # prints Block 0
print(blockchain.head.hash) # prints 9a80074454a08bd893afd50ad666803e636718850e57916174e535f504bed58d
print(blockchain.head.next) # prints None


print('\n----- Test Case 2 -----')
blockchain_2 = Blockchain()
blockchain_2.append_block('Block 0')
blockchain_2.append_block('Block 1')
blockchain_2.append_block('Block 2')
blockchain_2.append_block(None)
print(blockchain_2.head.data) # prints Block 0
next_block = blockchain_2.head.next
another_block = blockchain_2.head.next.next
print(next_block.hash == another_block.previous_hash) # prints True
print(next_block.data) # prints Block 1
print(another_block.data) # prints Block 2


print('\n----- Test Case 3 -----')
blockchain_3 = Blockchain()
blockchain_3.append_block('Block 0')
blockchain_3.append_block('Block 1')
blockchain_3.append_block('Block 2')
blockchain_3.append_block('Block 3')
blockchain_3.append_block('Block 4')
blockchain_3.append_block('Block 5')
print(blockchain_3.head.data) # prints Block 0
next_block = blockchain_3.head.next
another_block = blockchain_3.head.next.next
yet_another_block = blockchain_3.head.next.next.next
print(next_block.hash == another_block.previous_hash) # prints True
print(next_block.hash == yet_another_block.previous_hash) # prints False
print(next_block.data) # prints Block 1
print(another_block.data) # prints Block 2
print(yet_another_block.data) # prints Block 3