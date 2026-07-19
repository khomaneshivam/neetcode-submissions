class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums1 = []
        for i in range(len(nums)):
            x = 1
            for j in range(len(nums)):
                if i == j:
                    continue 
                else :
                    x *= nums[j]
            nums1.append(x)
        return nums1