'''
Problem:

在一个post 里面找出所有的name分别出现的位置，post 会很长

Follow-up: names 如果很多怎么办？
'''

'''
Follow-up: Use TrieTree,
word.length = k, post.length = n
Time complexity: O(nk), space complexity: total number of the node in trie tree
'''

class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.isWord = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        node = self.root
        for letter in word:
            if not node.children.has_key(letter):
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.isWord = True
        return

            
    def search(self, post, index):

        result = []
        word = ''
        node = self.root

        # index 和 node 都往前走
        # 走到 "not node.children.has_key(letter)"
        while index < len(post):
            if node.isWord:
                result.append(word)
            letter = post[index]
            if not node.children.has_key(letter):
                return result
            node = node.children[letter]
            word += letter
            index += 1

        if node.isWord:
            result.append(word)
        return result
        


    def findWords(self, words, post):
        if not words: return []
        
        result = collections.defaultdict(list)
        # add all words to the trie
        for word in words:
            self.insert(word)
        # for each index in post, search if any word starts from index i
        for i in range(len(post)):
            res = search(post, i)

            for word in res:
                result[word].append(i)

        return result

