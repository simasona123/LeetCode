class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        x = 0
        for i in nums:
            if i == 1:
                x += 1
            else:
                if x > max_consecutive :
                    max_consecutive = x
                x = 0
        if x > max_consecutive:
            max_consecutive = x
        return max_consecutive
