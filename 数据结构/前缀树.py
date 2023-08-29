"""
Author: ByronVon
Date: 2023-08-23 17:28:55
FilePath: /leetcode/数据结构/前缀树.py
Description: 
"""


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """实现前缀树的关键思想是利用树形结构的层级关系来表示字符串的字符序列。每一个节点可以有26个子节点，分别代表26个字母。"""

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            # 需要沿着某个节点纵向插入
            node = node.children[ch]
        node.is_end_of_word = True  # 插入结束，需要加入一个end的标志

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end_of_word

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


if __name__ == "__main__":
    trie = Trie()
    print(trie.insert("apple"))
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    print(trie.insert("app"))
    print(trie.search("app"))
