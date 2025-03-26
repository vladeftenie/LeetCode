class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        for c in s:
            if c in sMap:
                sMap[c] += 1
            else:
                sMap[c] = 1
        
        for c in t:
            if c not in sMap:
                return False
            else:
                sMap[c] -= 1

        for val in sMap.values():
            if val:
                return False
        
        return True