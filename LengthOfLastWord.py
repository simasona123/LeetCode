import re
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        non_char = 0
        char = 0
        for i in range(len(s)-1, -1, -1):
            if re.match("\S", s[i]) and non_char == 0:
                char += 1 
            if char > 0 and re.match("\s", s[i])  :
                break
            else:
                continue
                
        return char