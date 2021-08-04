from collections import deque
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left: int = 0
        answer: List[int] = []
        for item in nums:
            answer.append(item)
            if item % 2 == 0:
                temp = answer[left]
                answer[left] = item
                answer[-1] = temp
                left += 1
        return answer
    