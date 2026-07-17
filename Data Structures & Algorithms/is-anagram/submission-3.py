class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        f2 = {}
        for ch in s:
            freq1[ch] = freq1.get(ch, 0) + 1
        for ch in t:
            f2[ch] = f2.get(ch,0) + 1
        if freq1 == f2 :
            return True
        else :
            return False