class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        x = 0
        for i in nums:
            a = 1
            while i >= 10:
                i = i/10
                a += 1
            if a % 2 == 0:
                x += 1
        return x