class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer:List[int] = []
        len_nums = len(nums)
        nums = list(set(nums))
        before = 1
        for i in range (1, len_nums+1):
            if i not in nums:
                answer.append(i)
        return answer
#Time Limit Exceed