class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            first_item = strs[0]
            result = ""
            x = 0 
            if len(strs) == 1:
                return first_item
            for i in range(0, len(first_item)):
                for j in range(1, len(strs)):
                    if i > len(strs[j])-1:
                        x = 1
                        break
                    if j == len(strs)-1 and strs[j][i] == first_item[i]:
                        result = result + first_item[i]
                    elif strs[j][i] == first_item[i]:
                        continue
                    else: 
                        x = 1
                        break
                if x == 1 :
                    break
            return result
                        
                        
                    