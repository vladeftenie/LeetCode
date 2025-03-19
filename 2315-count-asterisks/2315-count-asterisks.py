class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum([start.count('*') for start in s.split("|")][0::2])
