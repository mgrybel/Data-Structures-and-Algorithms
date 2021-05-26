In Problem 3, Huffman Coding, a heap structure constructed using Python's heapq module is utilised to allow for easy addition and removal of the frequency nodes. 

huffman_encoding operation:

The time complexity of the huffman_encoding operation is O(n log n) because:
- O(n) - iterating through a given string and determining the frequency of each of the characters (get_frequencies function)
- O(n) - converting the data into a heap structure (get_heap function)
- O(log n) - the commands from the heapify module (combine_nodes function)
- O(n) - creating a dictionary of characters and their codes (get_codes function)
- O(n) - get_encoded_string function
Therefore, the total time complexity is O(n log n).

- The space complexity of the huffman_encoding operation is O(n) since n represents the size of a given string to be encoded. There is a linear space complexity.

huffman_decoding operation:

- The time complexity of the huffman_decoding operation is O(n) since we have here a for loop and we are looping through each of the characters in the encoded text. 
- The space complexity of the huffman_decoding operation is O(n) since n represents the size of a given string to be decoded. There is a linear space complexity.