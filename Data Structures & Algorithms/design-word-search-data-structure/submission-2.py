from collections import deque
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True
        return

    def search(self, word: str) -> bool:
        que = deque([self.root])
        # for each character in word
        for c in word:
            levelSize = len(que)
            
            # if there's nothign in the queue it means we had no viable options, so the search has failed
            if levelSize == 0:
                return False
            
            # consume everything in the que before adding more stuff to it 
            for _ in range(levelSize):
                node = que.popleft()
                # if we see a dot explor all possible options
                if c == ".":
                    for child in node.children.values():
                        que.append(child)
                else:
                    if c in node.children:
                        que.append(node.children[c])
        
        return any(node.isEnd for node in que)

        
