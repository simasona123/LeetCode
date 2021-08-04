class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_set = set()
        for item in arr:
            if item*2 in arr_set or item/2 in arr_set:
                return True
            arr_set.add(item)
        return False
