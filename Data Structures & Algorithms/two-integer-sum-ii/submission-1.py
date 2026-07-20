class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        left = 0
        right = len(num)-1
        result = []
        while left < right:
            if num[left] + num[right] == target :
                result.append(left + 1)
                result.append(right + 1)
                break
            elif num[left] + num[right] < target :
                left += 1
            elif num[left] + num[right] > target :
                right -= 1
           
        return result 


