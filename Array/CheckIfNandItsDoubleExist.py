class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_len = len(arr)
        for i in range (0, arr_len):
            x = arr[i]
            for j in range (i+1, arr_len):
                if x == 2*arr[j] or 2*x==arr[j]:
                    return True
        return False