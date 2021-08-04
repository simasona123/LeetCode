class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False    
        before = -1
        peak = 0
        x = 0
        for item in arr:
            if x == 0 and item > before: 
                pass
            elif before > item and x==0 :
                peak = before
                x += 1
            elif before == item :
                return False
            elif x != 0 :
                if item < before:
                    pass
                else :
                    return False
            before = item
        if peak == 0 or peak==arr[0]:
            return False
        return True