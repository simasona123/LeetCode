class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number_digit = len(digits)
        j = 0
        num = 0
        for i in range(number_digit-1, -1, -1):
            num += digits[j] * (10**i)
            j += 1
        num += 1
        j = []
        for item in str(num):
            j.append(int(item))
        return j
            