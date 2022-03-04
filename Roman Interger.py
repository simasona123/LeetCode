class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I' :1,
            'V' :5,
            'X' :10,
            'L' :50,
            'C' :100,
            'D' :500,
            'M' :1000,
        }
        
        result = 0
        previous = 0
        
        for i in reversed(s):
            result += roman[i]
            if roman[i] < previous:
                result -= roman[i]*2
            previous = roman[i]
        
        return result