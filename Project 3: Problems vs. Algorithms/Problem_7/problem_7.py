# Problem 7: Request Routing in a Web Server with a Trie


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, paths, handler):
        # Recursively add nodes
        # Assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for item in paths:
            if item not in node.children:
                node.insert(item)
            node = node.children[item]
        node.handler = handler

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for item in paths:
            if item not in node.children:
                return None
            node = node.children[item]
        return node.handler


# A RouteTrieNode similar to the autocomplete TrieNode with one additional element, a handler
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children and a handler
        self.children = {}
        self.handler = handler

    def insert(self, path):
        # Insert the node as before
        self.children[path] = RouteTrieNode()


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler=None, not_found = None):
        # Create a new RouteTrie for holding routes
        # Add a handler for 404 page not found responses
        self.route_trie = RouteTrie(handler)
        self.not_found = not_found

    def add_handler(self, path, handler):
        # Add a handler for a path
        # Split the path and pass the pass parts as a list to the RouteTrie
        self.route_trie.insert(self.split_path(path), handler)

    def lookup(self, path):
        # Lookup path (by parts) and return the associated handler
        # If it's not found, return the "not found" handler
        if path == "/":
            return self.route_trie.root.handler
        paths = self.split_path(path)
        result = self.route_trie.find(paths)
        if result is not None:
            return result
        else:
            return self.not_found

    def split_path(self, path):
        # Split the path into parts for both the add_handler and lookup functions
        paths = path.split("/")
        if paths[-1] == "":
            del paths[-1]
        return paths


# ---------- Test Cases ----------

# Create the router and add routes
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")
router.add_handler("/home/contact", "contact handler")
router.add_handler("/home/videos", "videos handler")
router.add_handler("/home/blog/news", "news handler")

# Lookups with the expected output
print(router.lookup("/"))                       # prints: root handler
print(router.lookup(""))                        # prints: root handler
print(router.lookup("/home"))                   # prints: not found handler
print(router.lookup("/home/about"))             # prints: about handler
print(router.lookup("/home/about/"))            # prints: about handler
print(router.lookup("/home/about/me"))          # prints: not found handler
print(router.lookup("/home/contact"))           # prints: contact handler
print(router.lookup("/home/videos"))            # prints: videos handler
print(router.lookup("/home/blog/news"))         # prints: news handler
print(router.lookup("/home/blog/news/videos"))  # prints: not found handler