class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_ones = 0
        len_nums = len(nums)
        for i in range (0, len_nums):
            temp_a = 0
            k_total = 0
            for j in range (i, len_nums):
                if nums[j] == 1:
                    temp_a += 1
                elif nums[j] == 0:
                    k_total += 1
                    if k_total > k:
                        break
                    temp_a += 1
            if temp_a > max_ones:
                max_ones = temp_a
        return max_ones

#Masih terlalu Lambat