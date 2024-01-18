class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_word = False

    def __iter__(self):
        if self.is_word:
            yield ""
        for ch, child in self.children.items():
            for word in child:
                yield ch + word


class TrieDictionary:
    def __init__(self):
        self.root = TrieNode("")

    def add(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode(ch)
            node = node.children[ch]
        node.is_word = True
        return self

    def __iter__(self):
        yield from self.root

# demo     
tree = TrieDictionary()
tree.add("sensitive").add("sense").add("senior").add("sentiment").add("sensible")
print(*tree)