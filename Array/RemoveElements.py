class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr_len = len(nums)
        i = 0
        shift = 0
        k = 0
        for item in nums :
            if item == val :
                shift += 1
                k += 1
            else :
                nums[i] = nums[i+shift]
                i += 1
        k = arr_len-k
        return k
    
    # you can use remove 