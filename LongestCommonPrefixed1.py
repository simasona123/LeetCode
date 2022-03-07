class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        max_length = len(strs[0])
        
        for i in range(len(strs)):
            if len(strs[i]) < max_length:
                max_length = len(strs[i])
                
            prefix = self.matched(prefix, strs[i])
            
        return prefix
        
    def matched(self, prefix, word):
        matchedString = ""
        for i in range(min(len(prefix), len(word))):
            if prefix[i] == word[i]:
                matchedString += prefix[i]
            else: 
                return matchedString
        return matchedString
