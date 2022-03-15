class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = nums[0]
        for i in range (len(nums)):
            curr = nums[i]
            answer = max(answer, curr)
            for j in range (i+1, len(nums)):
                curr += nums[j]
                answer = max(answer, curr)
            answer = max(answer, curr)
        return answer

# BruteForce Time Limit Exceed

class Solution:
    def maxSubArray(self, nums):
        curr, maxs = nums[0], nums[0]
        for i in range(1,len(nums)):
            curr = max(nums[i], curr+nums[i])
            maxs = max(curr, maxs)
        return maxs
            
#Kandane Algorithm

class Solution:
    def maxSubArray(self, nums):
        a = [*nums]
        for i in range(1, len(nums)):
            a[i] = max(a[i], a[i-1]+a[i])
        return max(a)            

#Tabulation Dynamic Programming

