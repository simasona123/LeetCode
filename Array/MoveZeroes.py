class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0 
        j = 0
        len_nums = len(nums)
        for x in range (0, len_nums):
            if nums[x]==0:
                j += 1
            else:
                nums[i]=nums[x]
                i += 1
        for x in range (len_nums-1, len_nums-j-1, -1):
            nums[x]=0
            
        