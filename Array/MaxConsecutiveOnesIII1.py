class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i:int = 0
        j:int = 0
        for item in nums :
            if item == 0:
                k -= 1
            if k < 0 :
                if nums[i] == 0:
                    k += 1
                i += 1
            j += 1
        return len(nums) - i 