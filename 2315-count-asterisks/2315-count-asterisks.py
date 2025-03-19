class Solution:
    def countAsterisks(self, s: str) -> int:
        read = True
        cnt = 0
        for c in s:
            if c == '|':
                read = not read
                continue
            if read and c == '*':
                cnt += 1
        return cnt
