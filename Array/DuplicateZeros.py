class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        skip = False
        
        for i in range(0, len(arr)):
            if arr[i] == 0 and not skip:
                arr.insert(i+1, 0)
                arr.pop()
                skip = True
            else:
                skip = False