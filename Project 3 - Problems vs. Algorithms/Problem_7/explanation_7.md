In Problem 7, Request Routing in a Web Server with a Trie, the Trie data structure is utilised to implement an HTTPRouter like we would find in a typical web server. There are three classes: RouteTrie, RouteTrieNode and Router.

RouteTrie insert:
- In order to insert, we must iterate through each path directory after splitting the path into parts, and store the results as TrieNodes (children of the previous directory). Therefore, the time complexity and space complexity are both O(n), where n represents the number of directories in the path.

RouteTrie find:
- In order to find a node, we must iterate through each directory of the path and examine if that directory is in the Trie. Therefore, the time complexity is O(n).
- The space complexity is O(1) because we store only the current node.

RouteTrieNode insert:
- The time complexity and space complexity are both O(1) because a TrieNode is only added to the children list of a current node, which is a dictionary.

Router add_handler:
- This is a wrapper for the RouteTrie insert. Therefore, it has the same time complexity and space complexity - both O(n), where n represents the number of directories in the path.

Router lookup:
- This is basically a wrapper for the RouteTrie find. First, the root handler is returned (constant), and if no handler was found, the not found handler is returned (also constant). Therefore, the time complexity is the same as that of the RouteTrie find - O(n), where n represents the number of directories in the path.
- The space complexity is O(n) because we store the paths for the find function.

Router split_path:
- The time complexity and space complexity are both O(n) because we have to store the number of directories within the path after splitting the path into parts.