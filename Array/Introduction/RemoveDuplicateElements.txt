class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr = []
        x = 0
        a = len(nums)
        for i in range (1, a):
            if nums[i] == nums[i-1]:
                arr.append(nums[i-1])
                x += 1
        for i in arr:
            nums.remove(i)
        return a - x