class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        answer: List[int] = []
        nums.sort()
        for i in range (len(nums)-1, -1, -1):
            if nums[i] not in answer:
                answer.append(nums[i])
            if len(answer) == 3:
                break
        if len(answer) != 3:
            return answer[0]
        else:
            return answer[2]
            