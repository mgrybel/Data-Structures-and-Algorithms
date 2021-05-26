# Problem 5: Autocomplete with Tries


# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix = ""):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        suffixes_list = []
        def traverse(node, current_suffix):
            if node.is_word:
                suffixes_list.append(current_suffix)
            for char in node.children:
                new_suffix = current_suffix + char
                traverse(node.children[char], new_suffix)
        traverse(self, "")
        return suffixes_list


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root

        for char in word:
            if char not in node.children:
                node.insert(char)
            node = node.children[char]
        node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        if type(prefix) != str:
            return "Invalid prefix"
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node


# ---------- Tests ----------

my_trie = Trie()
word_list = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]

for word in word_list:
    my_trie.insert(word)


print("Prefix: ant")
node = my_trie.find("ant")
print(", ".join(node.suffixes())) # prints: hology, agonist, onym


print("Prefix: f")
node = my_trie.find("f")
print(", ".join(node.suffixes())) # prints: un, unction, actory

print("Prefix: tri")
node = my_trie.find("tri")
print(", ".join(node.suffixes())) # prints: e, gger, gonometry, pod

print("Prefix: Empty string")
node = my_trie.find("")
print(", ".join(node.suffixes())) # prints: ant, anthology, antagonist, antonym, fun, function, factory, trie, trigger, trigonometry, tripod

print("Prefix: None")
node = my_trie.find(None)
print(node) # prints: Invalid prefix

print("Prefix: Number")
node = my_trie.find(365)
print(node) # prints: Invalid prefix