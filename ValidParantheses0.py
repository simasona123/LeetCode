class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        whitelist = { "(" : ")", "[" : "]", "{": "}" }
        
        open_bracket = []
        
        x = 0
        
        for i in s :
            for j in whitelist:
                if i == j:
                    open_bracket.append(i)
                    x = 1
                    break
            if x == 1:
                x = 0
                continue
            else:
                if len(open_bracket) == 0:
                    return False
                elif i == whitelist[open_bracket[-1]] :
                    open_bracket.pop()
                    continue
                else:
                    return False
        if len(open_bracket) > 0:
            return False
        return True
        
        
        