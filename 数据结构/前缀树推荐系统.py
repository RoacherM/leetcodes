"""
Author: ByronVon
Date: 2023-08-23 18:10:34
FilePath: /leetcode/数据结构/前缀树推荐系统.py
Description: 
"""

from bisect import bisect_left


class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.words.append(word)
            node.words.sort()
            if len(node.words) > 3:
                node.words.pop()

    def search(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        return node.words


def suggestedProducts(products, searchWord):
    trie = Trie()
    for product in sorted(products):
        trie.insert(product)
    return [trie.search(searchWord[: i + 1]) for i in range(len(searchWord))]


def suggestedProducts2(products, searchWord):
    products.sort()
    res, prefix, i = [], "", 0

    for c in searchWord:
        prefix += c
        # bisect_left被用来快速找到与给定前缀相匹配的第一个词。
        i = bisect_left(products, prefix, i)
        res.append([w for w in products[i : i + 3] if w.startswith(prefix)])

    return res


if __name__ == "__main__":
    # 测试
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    print(suggestedProducts2(products, searchWord))
