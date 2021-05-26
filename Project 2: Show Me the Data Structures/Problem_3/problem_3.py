# Problem 3: Huffman Coding

import sys
import heapq

class Huffman_Node:
    def __init__(self, index, frequency):
        self.index = index
        self.frequency = frequency
        self.left = None
        self.right = None

    def __gt__(self, other):
        if not other:
            return -1
        if not isinstance(other, Huffman_Node):
            return -1
        return self.frequency > other.frequency

class Huffman_Coding:

    def huffman_encoding(self, string):
        if string == "":
            return "", None
        frequencies = self.get_frequencies(string)
        min_heap = self.get_heap(frequencies)
        combined_heap = self.combine_nodes(min_heap)
        tree = heapq.heappop(combined_heap)
        codes = self.get_codes(tree)
        encoded_string = self.get_encoded_string(string, codes)
        return encoded_string, tree

    def huffman_decoding(self, encoded_string, tree):
        decoded_string = ""
        if encoded_string == "":
            return decoded_string
        node = tree
        for index in encoded_string:
            if index == '0':
                node = node.left
            else:
                node = node.right
            if node.index is not None:
                decoded_string += node.index
                node = tree
        return decoded_string  

    def combine_nodes(self, heap):
        if len(heap) == 1:
            node = heapq.heappop(heap)
            new_node = Huffman_Node(None, node.frequency)
            new_node.left = node
            heapq.heappush(heap, new_node)
        while len(heap) > 1:
            node_1 = heapq.heappop(heap)
            node_2 = heapq.heappop(heap)
            new_node = Huffman_Node(None, node_1.frequency + node_2.frequency)
            new_node.left = node_1
            new_node.right = node_2
            heapq.heappush(heap, new_node)
        return heap

    def get_codes(self, tree):
        if tree.left is None and tree.right is None:
            return {tree.index:'0'}
        return self.get_codes_rec(tree, "")

    def get_codes_rec(self, root, current):
        codes = {}
        if root is None:
            return {}
        if root.index is not None:
            codes[root.index] = current
        codes.update(self.get_codes_rec(root.left, current + "0"))
        codes.update(self.get_codes_rec(root.right, current + "1"))
        return codes

    def get_encoded_string(self, data, codes):
        encoded_string = ""
        for index in data:
            encoded_string += codes[index]
        return encoded_string

    def get_frequencies(self, data):
        frequencies = {}
        for index in data:
            if not index in frequencies:
                frequencies[index] = 0
            frequencies[index] += 1
        return frequencies

    def get_heap(self, frequencies):
        heap = []
        for frequency in frequencies:
            node = Huffman_Node(frequency, frequencies[frequency])
            heapq.heappush(heap, node)
        return heap
    

if __name__ == "__main__":

    huffman = Huffman_Coding()

    print('----- Test Case 1: A sentence -----')
    test_sentence = "The bird is the word"
    print ("The size of the data is: {}".format(sys.getsizeof(test_sentence))) # The size of the data is: 69
    print ("The content of the data is: {}".format(test_sentence)) # The content of the data is: The bird is the word
    encoded_data, tree = huffman.huffman_encoding(test_sentence)
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2)))) # The size of the encoded data is: 36
    print ("The content of the encoded data is: {}".format(encoded_data)) # The content of the encoded data is: 1000111111100100001101110000101110110110100011111111001101010011100001
    decoded_data = huffman.huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data))) # The size of the decoded data is: 69
    print ("The content of the encoded data is: {}".format(decoded_data)) # The content of the encoded data is: The bird is the word


    print('\n----- Test Case 2: A character -----')
    test_sentence = "m"
    print ("The size of the data is: {}".format(sys.getsizeof(test_sentence))) # The size of the data is: 50
    print ("The content of the data is: {}".format(test_sentence)) # The content of the data is: m
    encoded_data, tree = huffman.huffman_encoding(test_sentence)
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2)))) # The size of the encoded data is: 24
    print ("The content of the encoded data is: {}".format(encoded_data)) # The content of the encoded data is: 0
    decoded_data = huffman.huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data))) # The size of the decoded data is: 50
    print ("The content of the encoded data is: {}".format(decoded_data)) # The content of the encoded data is: m

    print('\n----- Test Case 3: Repeated single character -----')
    test_sentence = "aaaaaaaaaaaaaa"
    print ("The size of the data is: {}".format(sys.getsizeof(test_sentence))) # The size of the data is: 63
    print ("The content of the data is: {}".format(test_sentence)) # The content of the data is: aaaaaaaaaaaaaa
    encoded_data, tree = huffman.huffman_encoding(test_sentence)
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2)))) # The size of the encoded data is: 24
    print ("The content of the encoded data is: {}".format(encoded_data)) # The content of the encoded data is: 00000000000000 
    decoded_data = huffman.huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data))) # The size of the decoded data is: 63
    print ("The content of the encoded data is: {}".format(decoded_data)) # The content of the encoded data is: aaaaaaaaaaaaaa


    print('\n----- Test Case 4: Repeated characters and different letter case -----')
    test_sentence = "cccCCCgggGGG"
    print ("The size of the data is: {}".format(sys.getsizeof(test_sentence))) # The size of the data is: 61
    print ("The content of the data is: {}".format(test_sentence)) # The content of the data is: cccCCCgggGGG
    encoded_data, tree = huffman.huffman_encoding(test_sentence)
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2)))) # The size of the encoded data is: 28
    print ("The content of the encoded data is: {}".format(encoded_data)) # The content of the encoded data is: 000000101010010101111111
    decoded_data = huffman.huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data))) # The size of the decoded data is: 61
    print ("The content of the encoded data is: {}".format(decoded_data)) # The content of the encoded data is: cccCCCgggGGG