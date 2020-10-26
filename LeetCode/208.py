import numpy as np
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__trie = np.zeros([200000,26],dtype=np.int)
        self.__end = np.zeros(200000,dtype=np.int)
        self.__k = 1


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        p = 0
        for w in word:
            c = ord(w) - 97
            if not self.__trie[p][c]:
                self.__trie[p][c] = self.__k
                self.__k+=1
            p=self.__trie[p][c]
        self.__end[p] = 1



    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = 0
        for w in word:
            c = ord(w) - 97
            if not self.__trie[p][c]:
                return False
            p = self.__trie[p][c]
        return True if self.__end[p] else False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = 0
        for w in prefix:
            c = ord(w) - 97
            if not self.__trie[p][c]:
                return False
            p = self.__trie[p][c]
        return True

if __name__ == '__main__':
    trie = Trie()
    print(trie.insert("apple"))
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    print(trie.insert("app"))
    print(trie.search("app"))