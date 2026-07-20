class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        longest = 0
    
        for i in num:
            if i - 1 in num:
                continue
            n = i
            length = 1
            while n + 1 in num:
                n = n + 1
                length += 1
            longest = max(longest , length)
        return longest