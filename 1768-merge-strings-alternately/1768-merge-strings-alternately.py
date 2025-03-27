class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ''
        l1 = len(word1)
        l2 = len(word2)
        if l1 < l2:
            w = 2
            l = l1
        else:
            w = 1
            l = l2
        i = 0
        for i in range(l):
            word += word1[i] + word2[i]

        if w == 1:
            for j in range(i + 1, l1):
                word += word1[j]
        else:
            for j in range(i + 1, l2):
                word += word2[j]
        return word
        
        
